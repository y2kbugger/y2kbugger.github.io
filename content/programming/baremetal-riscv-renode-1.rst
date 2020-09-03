Baremetal RISC-V Renode - Part 1
################################

:date: 2020-05-21 17:48:03
:modified: 2020-05-21 17:48:03
:tags: baremetal, assembly
:author: zak kohler
:summary: My attempts at the exercises in K&R.
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3eFvejBEI9Qmr_scx1xpuCPMU_1BLAgQ5fxIjrCo0jmv0EnmVyIjUTE2WYtA0sd0aV6oCpb2TIG7xj35pttUYfxmq8fJzAQMEcY1F5Pivo8dOECxbql-qYTUHFIYL8LClxwZNONGlPwkeTvV8mZnv8x4g=w362-h479-no`

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78
  https://www.youtube.com/watch?v=D0VuYe77Wu0&list=PLb-MsRpo_wlLW0EWRpAqnbbDsf4kxSI1x

.. contents::

Background
==========

Why do this
-----------
The goal of this series explore the line between hardware and software while creating a minimal, vendor-free environment to write and play with toy operating systems.

What is baremetal?
------------------
In the non-embedded world, when you compile and link a C program into an executable you are doing so with the intention of running it *within* a specific operating system. When you compile baremetal or ``--freestanding`` you are telling the compiler that you intend to run this without relying on an operating system. The could be used, for example, to write an operating system. Alternatively it can be used to access the hardware of a system directly on an embedded system. Doing so you sacrifice things such as memory management, standard IO, thread/process control, etc. Because of this, you can also compile to run on a small RTOS or even an embedded linux system depending on the amount of system resources you have available.

When you use a commercial development platform, you will likely be provided with a cross compiling toolchain and so easy way to run within a small RTOS for example `freedom-e-sdk <https://github.com/sifive/freedom-e-sdk>`_. Alternatively, there are also attempts to make small, but hardware agonistic RTOS see `zephyr <https://www.zephyrproject.org/>`_

What is RISC-V?
---------------
Wikipedia

    RISC-V (pronounced "risk-five") is an open standard instruction set architecture (ISA) based on established reduced instruction set computer (RISC) principles. Unlike most other ISA designs, the RISC-V ISA is provided under open source licenses that do not require fees to use.

Obtain the source code
======================
To get started you will need to clone the repository. This includes all of the examples as well as the source for Renode simulator and gcc riscv tool chain.

Renode and GCC are git submodules so if you use ``--recursive`` you can get everything downloaded in one shot.

.. code-block:: giturl

   git clone --recursive git@github.com:y2kbugger/baremetal-riscv-renode.git

Toolchain compilation
=====================
Technically you could try to find these pre-compiled from your distro or elsewhere, but I suggest compiling from source to ensure we have matching versions and build options.

There are some compilation prerequisites and gotchas. If my package hints fail, just refer to the official project documentation for each.

Building
--------
I have added a ``Makefile`` which build the toolchains. If you have all of the build requirements already installed, building both can be as simple as:

.. code-block:: bash

    cd baremetal-riskv-renode
    make toolchains

Running it should usually be enough to let you know what you are missing. I have included some hints below, check the comments as well as different platforms may have different packages.

.. important::

    Make sure you have ``curses``/``ncurses`` headers.

    If they are missing the build will **succeed**, but you will **not be able to access** the GDB text user interface, TUI. This is import for being able to step through the source code. See the GCC hints.

Build requirement hints
-----------------------
Below are my hints for which packages to install, this can be different depending on the distribution. I've include links to the official guides should you get stuck on either.

gcc
^^^
https://github.com/riscv/riscv-gnu-toolchain

.. code::

    gawk texinfo bison flex libncurses5-dev libncursesw5-dev

The package ``libncurses*`` provides ``ncurses``, and  ``texinfo`` provides ``makeinfo``.

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

    source activate_toolchains.sh

Blinking a virtual LED
======================
This is the part where we see whether the toolchains are compiled correctly.

We will learn how to control Renode and band step through the source code using the GNU debugger, ``gdb``.

Since we are just getting familiar with the tools we'll start off with the 'Hello, World' of hardware projects, blinking an LED.

To build and run our first example within Renode:

.. code-block:: bash

    cd 1_blinky
    make launch

If everything went correctly, you should see something like this:

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dKs20yaz1biM2MWXyi7HAcI0pb-BHYDYD1XM92Al11dQPQ26OJY8YULAlHPHtduGETCN5Y5D6aXtkiFi3-9tB3RNtj4A687SGo765evyqri2TjKMCyQeNSLNfZ-SV52yXlIEar9iQj2aEzPKAmBGrQOA=w628-h449-no


- todo explain make monitor open monitor and type quit to shutdown renode.

What did we just do?
--------------------
The first thing that happened is that we built our image that will be loaded into Renode. You can think of the image like a ROM and Renode is the emulator.

.. code-block:: bash

    riscv32-unknown-elf-gcc baremetal.s baremetal.c -ggdb -O0 -o image -ffreestanding -nostdlib


riscv32-unknown-elf-gcc
  gnu compiler. This will compile, assemble any link source code. This is the special cross compiling variant that we built earlier which runs on you host architecture (e.g. x86), but outputs binaries for riscv32.
baremetal.s baremetal.c
  adsf


-ggdb  Turn on debugging symbols so that gdb can reference memory locations by name.
-O  Sets the optimization level, 0 for off
-o image  Name of the output ELF binary
-ffreestanding  don't use or require main. Don't assume we have an operating system.
-nostdlib  don't rely on c standard libraries being available.



Program code
------------

.. code-block:: asm

    .equ LED, 0x60000800

    .section .text
    .global _start

    _start:
            li a0, 0x00
            li a0, 0x00
            li a3, 0x1200000
            li a5, LED
    loop:
            addi a0, a0, 0x01
            bne a0, a3,  loop

    toggle_led:
            lw a4, 0x0(a5)
            xori a4, a4, 0x1
            sw a4, 0x0(a5)
            jump _start, t0

- explain reset vector TODO
- explain memory mapped hardware registers.

renode
------
- todo explain how we launched Renode
- explain reset vector TODO againg? for first time here instead?
- explain the platform and and command files for renode.


gdb tui
-------
- todo explain:
- how to step through code
- now to set breakpoint
- how to continue
- inspecting registers

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eVGqrh2Gm1lQJKH27cWNYUQO8fVTUAvM1FNZ_pUis0Upip6vEa4ZNGOh79vosxGnBtFcacVX8QRNDgKEeklwFnI9hs6WrAlnzpTDZIyyn1oyTclXxU4_IlzydFbb0UFDkm0CFMsU8f3KIEKY0OWxoPzQ=w354-h710-no

Miro Samek and the modern embedded course series
================================================
I will be loosing cloning MIROS following some of his videos in spirit. He does a great introduction to many concepts in embedded and I want to share that in a way that we don't need to have a real board.

Preview of next post
====================
