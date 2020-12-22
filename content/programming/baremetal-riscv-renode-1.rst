Baremetal RISC-V Renode - Part 1: Blinky
########################################

:date: 2020-12-22 00:11:42
:modified: 2020-12-22 00:11:42
:tags: baremetal, RISC-V, Renode, assembly, CPUs
:author: zak kohler
:summary: Explore the line between hardware and software while creating a minimal, vendor-free environment to write and play with toy operating systems.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3chg3Hd7-XPkvOum0SQv3f9EZ30vjZ3BB70OMbEqWVWO9GkvjOh-sBBWg-cU_oD2xo7jj4TTvQReAX-2F4HSt6OPOur1bb06A-fQZUti-STZ0clEEkYPsCrHAhMq2rVkKLU2psnCGzE_pfs5rIWrda0xg=w454-h669-no`

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78
  https://www.youtube.com/watch?v=D0VuYe77Wu0&list=PLb-MsRpo_wlLW0EWRpAqnbbDsf4kxSI1x

.. contents::
    :depth: 2

Background
==========

I'm exploring the line between hardware and software by creating a series of demos within a minimal, free and open source environment. These demos span from blinking an LED to implementing a toy operating system. The goal is to minimize parts of the system that we take for granted and gain a better understanding of computers and operating systems.

What is baremetal?
------------------
In the non-embedded world, when you compile and link a C program into an executable you are doing so with the intention of running it *within* a specific operating system. When you compile baremetal or ``-freestanding`` you are telling the compiler that you intend to run this without relying on an operating system. This could be used, for example, to write an operating system. Alternatively it can be used to access the hardware of a system directly on an embedded system. Doing so sacrifices higher level luxuries such as memory management, standard IO, thread/process control, etc. Because of this, sometimes it makes sense to run on a type of minimal OS optimized for embedded, e.g. a real time operating system or RTOS.

When you use a commercial development platform, you will likely be provided with a cross compiling toolchain and possibly an RTOS. For an example see `freedom-e-sdk <https://github.com/sifive/freedom-e-sdk>`_. Alternatively, there are also attempts to make small, but hardware agonistic RTOS see `zephyr <https://www.zephyrproject.org/>`_.

What is RISC-V?
---------------
RISC-V is an open alternative to ARM or x86.

Wikipedia

    RISC-V (pronounced "risk-five") is an open standard instruction set architecture (ISA) based on established reduced instruction set computer (RISC) principles. Unlike most other ISA designs, the RISC-V ISA is provided under open source licenses that do not require fees to use.

What is Renode?
---------------
Renode is a simulator designed for embedded firmware. What sets it apart is the goal of not only emulating CPUs and SOCs, but also entire boards with peripherals such as ethernet and even multi-node networks of devices.

Alternatives such as QEMU aren't as optimized for the embedded space.

An emulator that you might use for playing video game ROMs is specialized for a single platform. For example, in an emulator cpu, graphics chips, audio, memory-map, etc are fixed and optimized. Renode on the other hand configures each platform with a config file.

Source code
===========
To get started you will need to clone the repository. This includes all of the examples as well as the source for Renode simulator and GCC RISC-V toolchain.

Renode and GCC are linked via ``git submodule`` so if you use ``--recursive`` you can clone everything in one shot.

.. code-block:: giturl

   git clone --recursive https://github.com/y2kbugger/baremetal-riscv-renode.git

Toolchain compilation
=====================
Technically you could try to find these pre-compiled from your distro or elsewhere, but I suggest compiling from source to ensure we have matching versions and build options.

There are some compilation prerequisites and gotchas. If my hints don't help, just refer to the official project documentation for each.

Building
--------
To ease the burden on my own memory, I have added a ``Makefile`` to capture the various build options for the toolchains. If you have all of the build requirements already installed, building both can be as simple as:

.. code-block:: bash

    $ cd baremetal-riscv-renode
    $ make toolchains

Running ``make toolchains`` should usually be enough to let you know what you are missing. I have included some hints below, check the comments as well as different distros may have different packages.

Build requirement hints
-----------------------
Below are my hints for which packages to install, this can be different depending on the distribution. I've also included links to the official guides for getting unstuck.

gcc
^^^
https://github.com/riscv/riscv-gnu-toolchain

.. code::

    gawk texinfo bison flex libncurses5-dev libncursesw5-dev

The package ``libncurses5-dev*`` provides headers for ``ncurses``, and  ``texinfo`` provides ``makeinfo``.

Renode
^^^^^^
https://renode.readthedocs.io/en/latest/advanced/building_from_sources.html

Mono provides the runtime and C# compiler required for Renode. Installing it can be tricky on some distros and having a mono that is incomplete or outdated can lead to hard to understand errors. Make sure your whole system is up-to-date if you run into issues compiling Renode.

Arch
  Everything worked fine using the ``mono`` package from extra.
Ubuntu
  **Do not** use the mono from standard repos. Follow the instructions for ``mono-complete`` here https://www.mono-project.com/download/stable/.

.. code::

    automake autoconf libtool g++ coreutils policykit-1 libgtk2.0-dev screen uml-utilities gtk-sharp2 python3

The package ``coreutils`` provides ``realpath`` on Debian.

Activating the toolchains
=========================
Beyond here, we assume both renode and riscv-gcc are on your ``PATH``. To accomplish this, you can source this activation script.

.. code-block:: bash

    $ source activate-toolchains.sh

Blinking a virtual LED
======================
To verify and get familiar with the tools we'll start off with the "Hello, World" of hardware projects: blinking an LED.

Blinking a virtual "LED" involves a few steps:

1. Build **image** from source code
2. Launch the hardware **simulator** configured by the platform (repl) file
3. Load the image into **RAM** of the simulator


Just get it running
--------------------
First open up the project folder::

    $ cd 1_blinky

Then following command will handle all steps 1-3, we'll break this down later::

    $ make launch

If everything went correctly, you should see something like this:

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dKs20yaz1biM2MWXyi7HAcI0pb-BHYDYD1XM92Al11dQPQ26OJY8YULAlHPHtduGETCN5Y5D6aXtkiFi3-9tB3RNtj4A687SGo765evyqri2TjKMCyQeNSLNfZ-SV52yXlIEar9iQj2aEzPKAmBGrQOA=w628-h449-no
   :alt: blinky demo running

You should have also noticed the monitor window open up. This is used to control the running renode machine; the ``?`` command will list the rest. The tab completion is also very helpful.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3f6eXxClG8aqr6wk2twPPD-lXLA7C4vskcZkecZVwPlqSYNCrxrdtvzBSEgK0YLixLm3OuJzJeM63alK8B1ATSZUp594xdfz2u8-vQeMlTSLMRl_ihZHDEQtH4scresowV29jguNfTZpzdqeX1sTttQng=w442-h197-no
   :alt: renode monitor

Quit using ``q`` or ``quit``::

    (vexriscv-machine) quit

Alternatively you can kill renode using ``CTRL`` + ``C`` in the terminal that you launched it from.

Hardware configuration
----------------------
The hardware to will be simulated is defined using a renode specific platform description format [#renode-describing-platforms]_

vexriscv.repl::

    mem: Memory.MappedMemory @ sysbus 0x0
        size: 0x00040000

    cpu: CPU.VexRiscv @ sysbus

    gpio_out: GPIOPort.LiteX_GPIO @ sysbus 0x60000800
        type: Type.Out
        0 -> led0@0
        1 -> led1@0

    led0 : Miscellaneous.LED @ gpio_out 0
    led1 : Miscellaneous.LED @ gpio_out 1

I like this because we can make a very minimal hardware configuration, free from any vendor specific complexity. Besides the cpu and memory, we have a general purpose input output (GPIO) register mapped to memory location ``0x60000800``. The ``->`` makes a connection from the GPIO pins to the LEDs. I don't exactly know why we need both ``0 -> led0@0`` and ``@ gpio_out 0`` as it seems redundant; if anyone knows, please let me know. You'll also commonly see  ``->`` used for connecting interrupts.

To toggle the LED we will need to write a driver that knows how to control the GPIO by writing to it's register.

Blinky source code
------------------
This initial program is written exclusively in RISC-V assembly [#riscv-prgrammers-guide]_ this is simple enough that every instruction that gets executed can be traced to this source file.

The code to drive this GPIO device is dead simple, you just need to write data to the memory location that maps to the GPIO pins.

Note that the platform specifies the mapping of ``0x60000800`` to the GPIO register.

baremetal.s:

.. code-block:: asm

    .equ LED, 0x60000800
    .equ DELAY_COUNT, 9000000
    .equ LED_STATE_INITIAL, 0b00
    .equ LED_STATE_TOGGLE_MASK, 0b01

    .section .text
    .global _start
    _start:
            li a5, LED
            li a4, LED_STATE_INITIAL
            li a6, LED_STATE_TOGGLE_MASK
            sw a4, 0x0(a5)
    loop:
            li a0, DELAY_COUNT      # reset counter
    delay_loop:
            addi a0, a0, -1         # count down
            bnez a0, delay_loop
    toggle_led:
            lw a4, 0x0(a5)          # read in old led state
            xor a4, a4, a6          # toggle led state word
            sw a4, 0x0(a5)          # write new state
            jump loop, t0

Building an elf binary using gcc
================================
GCC will build an ELF binary based on our assembly source code. This binary is the ROM image and Renode is the emulator.

By default, gcc outputs a format called ELF. This format is understood and loaded by the OS, `i.e. linux, <https://lwn.net/Articles/631631/>`_. Renode also has the ability to understand ELF files and will load the sections into memory and put the program counter at the right spot to start executing [#renode-elf-start]_.


.. code-block:: bash

    riscv32-unknown-elf-gcc baremetal.s baremetal.c -ggdb -O0 -o image -ffreestanding -nostdlib

riscv32-unknown-elf-gcc
    gnu compiler. This compiles, assembles, and links input source code. This is the special cross compiling variant that we built earlier which runs on your host architecture (e.g. x86), but outputs binaries for riscv32.
baremetal.s
    Assemble source file.


-ggdb  Turn on debugging symbols so that gdb can reference memory locations by name.
-O  Sets the optimization level, 0 for off
-o image  Name of the output ELF binary
-ffreestanding  don't use or require main. Don't assume we have an operating system.
-nostdlib  don't rely on c standard libraries being available.

Interactively Debugging Renode
==============================
Pause and step though code that is running on the simulator.

Attaching the GNU Debugger
--------------------------
After launching, you may attach GDB using `make debug`. This connects to the GDB server already running within Renode. It uses a GDB script to store default configuration, such as breaking execution and starting the text user interface or TUI, which shows source code alongside the disassembly.

.. code-block:: bash

    $ make launch
    $ make debug

If you are familiar with GDB you know the power of setting breakpoint, inspecting stacks, and much much more.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3chg3Hd7-XPkvOum0SQv3f9EZ30vjZ3BB70OMbEqWVWO9GkvjOh-sBBWg-cU_oD2xo7jj4TTvQReAX-2F4HSt6OPOur1bb06A-fQZUti-STZ0clEEkYPsCrHAhMq2rVkKLU2psnCGzE_pfs5rIWrda0xg=w454-h669-no
   :alt: gdb tui
   :align: left

   GDB Text User Interface (TUI)


Useful GDB scenarios
--------------------
There are a couple simple commands that I find to be useful when exploring baremetal programming.

Step a single instruction
^^^^^^^^^^^^^^^^^^^^^^^^^

Type ``S`` ``I`` ``Enter``

.. code-block:: gdb

    (gdb) si
    (gdb) █

To repeat the last command, just repeatedly hit ``Enter``. This makes it easy to single step through the program.

You will notice that you get stuck in the delay loop, you would have to hit ``Enter`` 9,000,000 times to make it though that delay. This is not a good way to add delays since it uses 100% of the CPU. If we were building an operating system, we could utilize a hardware timer and allow programs to request sleeps through an API. During the sleep the OS could go about running other processes, and then wake up the sleeping process at the appropriate time.

Continue normal execution
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: gdb

    (gdb) c
    Continuing.

Break normal execution
^^^^^^^^^^^^^^^^^^^^^^

Send a keyboard interrupt, e.g. ``CTRL`` + ``C``

.. code-block:: gdb

    (gdb) c
    Continuing.

    Program received signal SIGTRAP, Trace/breakpoint trap.
    delay_loop () at baremetal.s:13
    (gdb) █

Set a breakpoint
^^^^^^^^^^^^^^^^

You can set a breakpoint at a line or symbol. Tab completion should work here to display available symbols. So ``B`` ``Space`` ``T`` ``Tab`` ``Enter``

.. code-block:: gdb

    (gdb) b toggle_led
    Breakpoint 1 at 0x10074: file baremetal.s, line 16.
    (gdb) c
    Continuing.

    Breakpoint 1, toggle_led () at baremetal.s:16
    (gdb) █

Read Registers
^^^^^^^^^^^^^^

You can dump all registers,

.. code-block:: gdb


    (gdb) info registers
        ra             0x0      0x0
        fp             0x0      0x0
        s1             0x0      0
        a0             0x24648f 2385039
        ...
        t4             0x0      0
        t5             0x0      0
        t6             0x0      0
        pc             0x1006c  0x1006c <delay_loop>

or you can print a specific one:

.. code-block:: gdb

    (gdb) p $pc
    $5 = (void (*)()) 0x10074 <toggle_led>
    (gdb) p $a4
    $6 = 2

Setting a register
^^^^^^^^^^^^^^^^^^

You can mutate a register value and continue on:

.. code-block:: gdb

    (gdb) set $pc=delay_loop
    (gdb) c
    Continuing.

Changing the bitmask for blinky
===============================
Let's do something fun and prove we can modify a program's state after breaking.

If we just run the blinky example, note that we are blinking ``led0``:

.. code-block:: text

    15:09:23.7671 [NOISY] gpio_out.led0: LED state changed to True
    15:09:24.0805 [NOISY] gpio_out.led0: LED state changed to False
    15:09:24.3872 [NOISY] gpio_out.led0: LED state changed to True
    15:09:24.7525 [NOISY] gpio_out.led0: LED state changed to False

Change the bitmask:

.. code-block:: gdb

    (gdb) set $a6=0b10
    (gdb) c
    Continuing.

Now we are blinking ``led1`` instead of ``led0``:

.. code-block:: text

    15:09:42.5007 [NOISY] gpio_out.led1: LED state changed to True
    15:09:42.7653 [NOISY] gpio_out.led1: LED state changed to False
    15:09:43.0602 [NOISY] gpio_out.led1: LED state changed to True
    15:09:43.3263 [NOISY] gpio_out.led1: LED state changed to False

Miro Samek and the modern embedded course series
================================================
I am inspired by Miro Samek. He does a great introduction to many embedded programming concepts and I want to share that in a way that we don't need to have a real board.

Check out his course here: https://www.state-machine.com/quickstart/

Next post
=========
In the next post, I'll talk about alternate dev environments and how I converged on what I've described here. There are many easier and more *complete/integrated* solutions, but we have a stated goal of gaining understanding and this is a forcing function for more control over details.

Footnotes
=========
.. [#renode-elf-start] The computer has to start executing somewhere on reset, the exact memory location is called the reset vector and on RISC-V it is implementation dependent and Renode coordinates the reset vector in its simulator with the memory address of the `e_entry header <https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html>`_.

    `Renode changes the reset vector based on the ELF binary <https://github.com/renode/renode-infrastructure/blob/8ad326eefe85acc127fdb01d70dbbc9a6a99dca8/src/Emulator/Peripherals/Peripherals/CPU/TranslationCPU.cs#L107>`_

    .. code-block:: csharp

        this.Log(LogLevel.Info, "Setting PC value to 0x{0:X}.", elf.GetEntryPoint());
        SetPCFromEntryPoint(elf.GetEntryPoint());
.. [#renode-machine] https://renode.readthedocs.io/en/latest/basic/machines.html
.. [#renode-describing-platforms] https://renode.readthedocs.io/en/latest/basic/describing_platforms.html
.. [#riscv-prgrammers-guide] https://github.com/riscv/riscv-asm-manual/blob/master/riscv-asm.md
