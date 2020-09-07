Baremetal RISC-V Renode - Part 1: Blinky
########################################

:date: 2020-05-21 17:48:03
:modified: 2020-05-21 17:48:03
:tags: baremetal, assembly
:author: zak kohler
:summary: Explore the line between hardware and software while creating a minimal, vendor-free environment to write and play with toy operating systems.
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3dpMyfpSU2fcKBVPje2OZukgNuYhAubg0xkc6ycUbfd-OcxDFhj_bQ4OJL_vb5riU6mzwl9lKCACZT-DHryR9M3IJmk5DJ9oBN1-Vt29PM3DW_qe5cbSrrhRbMOc557s5uCDQOnBEw4WXLsEik6EXt4_A=w526-h295-no`

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78
  https://www.youtube.com/watch?v=D0VuYe77Wu0&list=PLb-MsRpo_wlLW0EWRpAqnbbDsf4kxSI1x

.. contents::
    :depth: 2

Background
==========

The baremetal risc-v renode series
----------------------------------
This series seeks to explore the line between hardware and software while creating a minimal, vendor-free environment to write and play with toy operating systems.

What is baremetal?
------------------
In the non-embedded world, when you compile and link a C program into an executable you are doing so with the intention of running it *within* a specific operating system. When you compile baremetal or ``-freestanding`` you are telling the compiler that you intend to run this without relying on an operating system. The could be used, for example, to write an operating system. Alternatively it can be used to access the hardware of a system directly on an embedded system. Doing so sacrifices higher level luxuries such as memory management, standard IO, thread/process control, etc. Because of this, sometimes it makes sense to run on a type of minimal OS optimized for embedded, e.g. a real time operating system (RTOS).

When you use a commercial development platform, you will likely be provided with a cross compiling toolchain and an RTOS. For an example see `freedom-e-sdk <https://github.com/sifive/freedom-e-sdk>`_. Alternatively, there are also attempts to make small, but hardware agonistic RTOS see `zephyr <https://www.zephyrproject.org/>`_

What is RISC-V?
---------------
Wikipedia

    RISC-V (pronounced "risk-five") is an open standard instruction set architecture (ISA) based on established reduced instruction set computer (RISC) principles. Unlike most other ISA designs, the RISC-V ISA is provided under open source licenses that do not require fees to use.

What is Renode?
---------------
Renode is a simulator designed for embedded firmware. What sets it apart is the goal of not only emulating CPUs and SOCs, but also entire boards with peripherals such as ethernet and even multi-node networks of devices.

Alternatives such as QEMU aren't as optimized for the embedded space.

An emulator that you might use for playing video game ROMs is specialized for a single platform, i.e. things like cpu, graphics chips, audio, memory-map, etc are fixed and optimized. Renode on the other hand configures each platform with a config file. 

Obtain the source code
======================
To get started you will need to clone the repository. This includes all of the examples as well as the source for Renode simulator and gcc riscv tool chain.

Renode and GCC are git submodules so if you use ``--recursive`` you can get everything downloaded in one shot.

.. code-block:: giturl

   git clone --recursive git@github.com:y2kbugger/baremetal-riscv-renode.git

Toolchain compilation
=====================
Technically you could try to find these pre-compiled from your distro or elsewhere, but I suggest compiling from source to ensure we have matching versions and build options.

There are some compilation prerequisites and gotchas. If my hints don't help, just refer to the official project documentation for each.

Building
--------
I have added a ``Makefile`` to capture the various build options for the toolchains. If you have all of the build requirements already installed, building both can be as simple as:

.. code-block:: bash

    $ cd baremetal-riskv-renode
    $ make toolchains

Running ``make toolchains`` should usually be enough to let you know what you are missing. I have included some hints below, check the comments as well as different platforms may have different packages.

Build requirement hints
-----------------------
Below are my hints for which packages to install, this can be different depending on the distribution. I've include links to the official guides should you get stuck on either.

gcc
^^^
https://github.com/riscv/riscv-gnu-toolchain

.. code::

    gawk texinfo bison flex libncurses5-dev libncursesw5-dev

The package ``libncurses5-dev*`` provides headers for ``ncurses``, and  ``texinfo`` provides ``makeinfo``.

Renode
^^^^^^
https://renode.readthedocs.io/en/latest/advanced/building_from_sources.html

Mono provides CLR runtime and C# compiler required for Renode. Installing it can be tricky on some distros and having a mono that is incomplete or outdated can lead to hard-to-understand errors. Make sure your whole system is up-to-date if you run into issue compiling Renode.

Arch
  Everything worked fine using the ``mono`` package from extra.
Ubuntu
  **Do not** use the mono from standard repos. Follow instruction for ``mono-complete`` here https://www.mono-project.com/download/stable/.

.. code::

    automake autoconf libtool g++ coreutils policykit-1 libgtk2.0-dev screen uml-utilities gtk-sharp2 python3

The package ``coreutils`` provides ``realpath`` on Debian.

Activating the toolchains
=========================
In order to run renode and gdb, you must put them on your ``PATH``.

.. code-block:: bash

    $ source activate-toolchains.sh

Blinking a virtual LED
======================
To verify and get familiar with the tools we'll start off with the 'Hello, World' of hardware projects: blinking an LED.

Blinking a virtual "LED" involves a few steps:

1. Build **image** from source code
2. Launch the hardware **simulator** configured by the platform (real) file
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

You should have also noticed the monitor window open up. This is used to control the running renode machine; ``?`` will show a list of what commands are available. The tab completion is also very helpful.

Quit using ``q`` or ``quit``::

    (vexriscv-machine) quit

Alternatively you can ``ctrl-c`` in the original terminal window kill renode.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fnOWf9q-DJAwfFMefjlX6-CqAgGpGfDzBTi36NOuASben_jmeDlka0AlgziFE5yXRDwnwLE16sFeVXKcKaIfjMaLDhFeLXYv9baJi8OI7C5Hhk35XOuAY78VAZiGmhAJT7GSi0ItsGKk1oQSAnoWN6Tg=w318-h92-no
   :alt: renode quitting

Hardware configuration
----------------------
The hardware that will be simulated is defined in the using a renode specific platform description format [#renode-describing-platforms]_

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

I like this because we can make a very minimal hardware configuration, free from any vendor specific complexity. Besides the cpu and memory, we have a GPIO register mapped to memory location ``0x60000800``. The ``->`` makes a connection from the GPIO pins to the LEDs.

To toggle the LED we will need to write a driver that knows how to control the GPIO by writing to the register.

- todo: toggle led by manually editing memory using gdb

Blinky manually with gdb
------------------------
Manually blink led by ediiting memory

Blinky source code
------------------
This initial program is written exclusively in risc-v assemble [#riscv-prgrammers-guide]_ this is simple enough that every instruction that gets executed can be traced to this source file.

The code to drive a GPIO device is dead simple, You just need to write a data to a memory location that maps to GPIO pins. 

draw a memory map table to explain the GPIO register

=====  ======  ======
adf    Inputs  Output
-----  ------  ------
  A      B     A or B
=====  ======  ======
False  False   False
True   False   True
False  True    True
True   True    True
=====  ======  ======

I want them to go into the source code and change the XOR bitmask

baremetal.s:

.. code-block:: asm

    .equ LED, 0x60000800
    .equ DELAY_COUNT, 9000000

    .section .text
    .global _start
    _start:
            li a5, LED
    loop:
            li a0, DELAY_COUNT      # reset counter
    delay_loop:
            addi a0, a0, -1         # count down
            bnez a0, delay_loop
    toggle_led:
            lw a4, 0x0(a5)          # read in old led state
            xori a4, a4, 0b01       # toggle led state word
            sw a4, 0x0(a5)          # write new state
            jump loop, t0

- todo which approach?? both? breakpoint and continue, or edit register;
- todo teach howoto stop through program using gdb. explain the need to lower the delay_count (you can do it in situ via register hack)
- todo inspecting registers
- todo how to step through code
- todo now to set breakpoint
- todo how to continue
- todo change led mask in situ?

Building an elf binary using gcc
--------------------------------
GCC will build am image based on our assembly source code. In video game terms, the image like a ROM and Renode is the emulator.

By default, gcc outputs a format called ELF. This format is understood and loaded by the OS, `i.e. linux, <https://lwn.net/Articles/631631/>`_. Renode also has the ability to understand ELF files and will load the sections into memory and put the program counter at the right spot to start executing [#renode-machine]_.

- explain reset vector TODO

.. code-block:: bash

    riscv32-unknown-elf-gcc baremetal.s baremetal.c -ggdb -O0 -o image -ffreestanding -nostdlib

riscv32-unknown-elf-gcc
    gnu compiler. This will compile, assemble any link source code. This is the special cross compiling variant that we built earlier which runs on you host architecture (e.g. x86), but outputs binaries for riscv32.
baremetal.s
    Assemble source file.


-ggdb  Turn on debugging symbols so that gdb can reference memory locations by name.
-O  Sets the optimization level, 0 for off
-o image  Name of the output ELF binary
-ffreestanding  don't use or require main. Don't assume we have an operating system.
-nostdlib  don't rely on c standard libraries being available.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eVGqrh2Gm1lQJKH27cWNYUQO8fVTUAvM1FNZ_pUis0Upip6vEa4ZNGOh79vosxGnBtFcacVX8QRNDgKEeklwFnI9hs6WrAlnzpTDZIyyn1oyTclXxU4_IlzydFbb0UFDkm0CFMsU8f3KIEKY0OWxoPzQ=w354-h710-no
   :alt: gdb tui

Miro Samek and the modern embedded course series
================================================
I will be loosing cloning MIROS following some of his videos in spirit. He does a great introduction to many concepts in embedded and I want to share that in a way that we don't need to have a real board.

Preview of next post
====================

.. [#renode-machine] https://renode.readthedocs.io/en/latest/basic/machines.html
.. [#renode-describing-platforms] https://renode.readthedocs.io/en/latest/basic/describing_platforms.html
.. [#riscv-prgrammers-guide] https://github.com/riscv/riscv-asm-manual/blob/master/riscv-asm.md

