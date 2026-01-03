---
title: LC-3 CPU emulator in pure SQL
date: 2025-12-26 10:06:02
tags: assembly, algorithms, CPUs, emulation, sql
author: zak kohler
summary: An LC-3 CPU emulator in pure SQL, using tables for state and triggers for transitions.
status: published
cover: /img/2025-12-26__lc3_sql__cover_screenshot.png
---

SQL may be a perverse platform to implement a CPU emulator on, but works well for a demo because all it requires is the SQLite cli binary to run.

A demo program that calculates pi is used to exercise the emulator.

[run it yourself](https://gist.github.com/y2kbugger/213912550ab7599e27b56a017bc94ad5)

> ```
> time sqlite3 :memory: < PISPIGOT69.sql
> ```
>
> Output

>     Runtime error near line 1289: HALT encountered (19)
>     Calculated first 69 digits of pi: 314159265358979323846264338327950288419716939937510582097494459230781
>     Ran for 8464947 clock cycles before halting.
>
>     real    0m45.428s

## Methodology
1. The pi spigot algorithm is written in ASM
2. ASM is assembled to machine code
3. A harness instantiates the cpu emulator in sql `TABLE`s and `TRIGGER`s
4. The harness loads the machine code into memory table with `INSERT`s
5. The cpu is clocked via a recursive cte until `HALT`ed
6. Then we can just trace out the db connection to distill to pure sql script.

## LC-3 Emulator in SQL
State is stored in tables. Surprisingly few tables were required, and only `register` is specific to the LC-3 instruction set.


``` sql
-- inserts here trigger the cpu to step.
CREATE TABLE clkt(
    value INT
    );

-- tracks the halt state and current instruction
CREATE TABLE signal(
    is_running BOOLEAN,
    instr INT
    );
INSERT INTO signal VALUES (
    FALSE,
    0
    );

CREATE TABLE register(
    id INT PRIMARY KEY,
    value INT
    );
INSERT INTO register VALUES
    (0, 0),   -- R0
    (1, 0),   -- R1
    (2, 0),   -- R2
    (3, 0),   -- R3
    (4, 0),   -- R4
    (5, 0),   -- R5
    (6, 0),   -- R6
    (7, 0),   -- R7
    (32, 0),  -- PC
    (64, 0);  -- COND

CREATE TABLE memory(
    address INT UNIQUE,
    value INT
    );

-- buffers for input and output messages
CREATE TABLE msgout (msg TEXT, channel TEXT);
```

## Clocking and instruction loading
The CPU is clocked by inserting into the `clkt` table. This fires a trigger. Originally clk was part of the signal table, but separating it out let us trigger on `INSERT`s rather than `UPDATE`s, but update required one statement for EVERY clock cycle.

``` sql
-- inserts here trigger the cpu to step.
CREATE TABLE clkt(
    value INT
    );

-- load instructions
CREATE TRIGGER clk_trigger
AFTER  INSERT ON clkt
BEGIN
    UPDATE signal
        SET instr = (
            (SELECT value FROM memory WHERE address = (SELECT value FROM register WHERE id = 32))
        );
END;

-- step Program Counter (PC) register
CREATE TRIGGER instr_trigger
BEFORE UPDATE OF instr ON signal
BEGIN
    UPDATE register
        SET value = value + 1
        WHERE id = 32;
END;
```

My first attempt at clocking was to `UPDATE` a clock field in the signal table, but that required one statement per clock cycle.
``` sql
UPDATE signal SET clk = 1;
UPDATE signal SET clk = 1;
UPDATE signal SET clk = 1;
UPDATE signal SET clk = 1;
UPDATE signal SET clk = 1;
UPDATE signal SET clk = 1;
...
```

By separating out the clock into its own table, I could `INSERT INTO` it via a recursive CTE (or the equivalent [`generate_series`](https://sqlite.org/series.html)) to clock an arbitrary number of steps in a single statement.

``` sql
-- step n instructions
BEGIN;
    INSERT INTO clkt(value)
    SELECT value
    FROM generate_series(1, 8500000);
COMMIT;
```

While there is logic to short circuit cycles when `HALT`ed, it still runs every clkt `INSERT`, so pick a number just beyond what you expect the program to need.

## Instruction decoding and execution
All that remains is to decode and execute the instruction that was just loaded into the `signal.instr` field. To fully implement the LC-3 instruction set, with a handful of `TRAP`s for I/O, It took about 420 lines of  well spaced triggers.

### System calls
`TRAP`s aka software interrupts allow interacting with the world.

`HALT` stops the machine
``` sql
-- ## TRAP x25 (HALT) ##
CREATE TRIGGER instr_hlt_trigger
AFTER UPDATE OF instr ON signal
    WHEN NEW.instr = 0xF025
BEGIN
    UPDATE signal SET is_running = 0;
    SELECT RAISE(FAIL, 'HALT encountered');
END;
```


`PUTS` outputs a string.
``` sql
-- ## TRAP x22 (PUTS) ##
DROP TRIGGER IF EXISTS instr_puts_trigger;

CREATE TRIGGER instr_puts_trigger
AFTER UPDATE OF instr ON signal
    WHEN NEW.instr = 0xF022
BEGIN

    -- PUTS implementation: read characters until null terminator
    INSERT INTO msgout
    SELECT group_concat(char(value), ''), 'output'
    FROM (
        SELECT value
        FROM memory
        WHERE address >= (SELECT value FROM register WHERE id = 0)
          AND address < COALESCE(
                (SELECT MIN(address) FROM memory
                 WHERE address >= (SELECT value FROM register WHERE id = 0)
                   AND value = 0),
                0x10000)  -- if no null terminator, go all the way!
        ORDER BY address
    );
END;
```

### Standard instructions
There are instructions for arithmetic, logic, memory access, and control flow.

Here is an example of the `ADD` instruction.

| Instruction | Operation |
|-------------|-----------|
| `ADD DR, SR1, SR2` | DR = SR1 + SR2 |
| `ADD DR, SR1, imm5` | DR = SR1 + imm5 |
``` sql
CREATE TRIGGER instr_add_trigger
AFTER UPDATE OF instr ON signal
    WHEN NEW.instr & 0xF000 = 0x1000
BEGIN
    UPDATE register
        SET value = ((SELECT value FROM register WHERE id = (NEW.instr >> 6) & 0x7)  -- SR1
                    + (CASE
                        WHEN (NEW.instr & 0x0020) != 0 THEN  -- immediate mode (bit 5 set)
                            CASE
                                WHEN (NEW.instr & 0x0010) != 0 THEN  -- sign extend negative imm5
                                    (NEW.instr & 0x001F) | 0xFFE0
                                ELSE
                                    (NEW.instr & 0x001F)             -- positive imm5 unchanged
                                END
                        ELSE  -- register mode (bit 5 clear)
                            (SELECT value FROM register WHERE id = NEW.instr & 0x7)  -- SR2
                        END)) & 0xFFFF  -- wrap at 16-bit
        WHERE id = (NEW.instr >> 9) & 0x7;  -- destination register DR

    UPDATE register
        SET value = (CASE
            WHEN (SELECT value FROM register WHERE id = (NEW.instr >> 9) & 0x7) = 0 THEN 2 -- Z
            WHEN (SELECT value FROM register WHERE id = (NEW.instr >> 9) & 0x7) >> 15  == 0 THEN 1 -- P
            ELSE 4 -- N
            END)
        WHERE id = 64;
END;
```

## Loading programs
Load machine code into memory and reset the CPU registers via `INSERT`s and `UPDATE`s.

``` sql
-- ... hundreds before ...
INSERT INTO memory (address, value) VALUES (12337, 57929);
INSERT INTO memory (address, value) VALUES (12338, 21664);
INSERT INTO memory (address, value) VALUES (12339, 22240);
INSERT INTO memory (address, value) VALUES (12340, 5878);
INSERT INTO memory (address, value) VALUES (12341, 6147);
INSERT INTO memory (address, value) VALUES (12342, 2051);
INSERT INTO memory (address, value) VALUES (12343, 4099);
INSERT INTO memory (address, value) VALUES (12344, 5281);
INSERT INTO memory (address, value) VALUES (12345, 4091);
INSERT INTO memory (address, value) VALUES (12346, 28736);
-- ... hundreds more ...
BEGIN;
    UPDATE register SET value = 0;
    DELETE FROM msgout WHERE channel = 'output';
    UPDATE signal SET is_running = 1;
COMMIT;
-- now ready to start clocking
```


## LC-3

The LC-3 is a simple 16-bit educational CPU architecture often used in computer architecture courses. It has a small instruction set and is designed to be easy to understand.

- 16-bit address space (64KB)
- 16-bit data words
- 16-bit instructions
- 8 general-purpose registers (R0-R7)

One reason I chose it because it was the simplest ISA claiming to have a C compiler.

### LC-3 Annoyances
Toolchains for LC-3 are never battle-tested. Existing implementations of the assemblers, emulators, and the C compilers are buggy. The source code that goes along with the textbooks is often incomplete because they expect you to implement parts of it as exercises.

There was also a lack of verification tests and software to run.

If I had to do it again, I would pick 6502, and I could choose from a plethora of verification ROMs to test against. And there are tons of retro games to port.

## Testing Strategy
I built a test harness in Python that can compare a reference Python implementation against the SQL implementation.
This actually worked out really well after gathering some programs for integration tests.

The integration tests compared full traces of register state. One day maybe I'll also add memory mutation tracing as well.

The test harness did the heavy lifting of loading programs into memory, stepping the CPU, as well as debugging features such as reading output, providing input, peeking and poking memory and registers, and using asm symbols as breakpoints for testing intermediate states.

See the [lc3_test_harness repo](https://github.com/y2kbugger/y2k-lc3-tools)

## Interactive Notebooks
Various interactive notebook tools:

- Assembling LC-3 assembly to machine code
- Disassembling machine code to LC-3 assembly
- Running LC-3 machine code in the SQL VM, while graphically debugging registers.
- Run and display results of sql snippets against a live LC-3 cpu instance.
  - E.g. peek at memory, registers, output buffer, etc.
  - Modifying triggers which implementing instructions on the fly.

### Raw SQL notebook magic `%%sql`

![SQL magic screenshot](/img/2025-12-26__lc3_sql__sql_magic_screenshot.png)

### SQLVM widget

![LC-3 SQL VM interactive widget screenshot](/img/2025-12-26__lc3_sql__pispigot_ipynb.apng)

