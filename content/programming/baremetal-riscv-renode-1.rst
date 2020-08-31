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
The goal of this series explore the line between hardware and software while creating a minimal, vendor-free environment to play with toy operating systems.

What is baremetal?
------------------
In the non-embedded world, when you compile and link a C program into an executable you are doing so with the intention of running it *within* a specific operating system. When you compile baremetal or ``--freestanding`` you are telling the compiler that you intend to run this without relying on an operating system. The could be used, for example, to write an operating system. Alternatively it can be used to access the hardware of a system directly on an embedded system. Doing so you sacrifice things such as memory management, standard IO, thread/process control, etc. Because of this, you can also compile to run on a small RTOS or even an embedded linux system depending on the amount of system resources you have available.

When you use a commercial development platform, you will likely be provided with a cross compiling toolchain and so easy way to run within a small RTOS for example `freedom-e-sdk <https://github.com/sifive/freedom-e-sdk>`_. Alternatively, there are also attempts to make small, but hardware agonistic RTOS see `zephyr <https://www.zephyrproject.org/>`_

What is RISC-V?
---------------
Wikipedia

    RISC-V (pronounced "risk-five") is an open standard instruction set architecture (ISA) based on established reduced instruction set computer (RISC) principles. Unlike most other ISA designs, the RISC-V ISA is provided under open source licenses that do not require fees to use.

Toolchain setup
===============
you can get these from anywhere, but i suggesting compiling from source to ensure we have matching versions. For gcc be aware you have compile the cross-compiling toolchain for rv32i.

There are some compilation prerequisites and gotchas. If my package hints fail, just refer to the official project documentation for each.

To get started, clone my repo, including sub repos:

.. code-block:: giturl

   git clone --recursive git@github.com:y2kbugger/baremetal-riscv-renode.git

Install the build requirements, using the hints below if you have trouble. Then build the toolchains:

.. code-block:: bash

    cd baremetal-riskv-renode
    make toolchains

gcc
---
https://github.com/riscv/riscv-gnu-toolchain

Packages I needed on my system

.. code::

    gawk, makeinfo(texinfo package), bison, flex

on an ubuntu test system i noticed that if you are missing a curses header, gdb will silently build without the text user interface tui.

.. code::

    libncurses5-dev libncursesw5-dev


renode
------
https://renode.readthedocs.io/en/latest/advanced/building_from_sources.html#building-from-source

mono-complete

- Arch: i think everything worked fine using the mono package.
- Ubuntu: I had inexplicable issues when installing from the standard repos. Following the mono site https://www.mono-project.com/download/stable/ worked great.

some other misc packages that i needed.

.. code::

    automake autoconf libtool g++ realpath(coreutils on debian) policykit-1 libgtk2.0-dev screen uml-utilities gtk-sharp2 python3

Blinking the virtual led
========================
For the first part of this series, we'll cover the minimal viable demo which blinks an LED. This will allow us to get started using renode, gcc riscv cross compiling, and using gdb.

To build and run our first example within renode:

.. code-block:: bash

    source activate_toolchains.sh
    cd 1_blinky
    make launch

If everything went correctly, you should see something like this:

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dKs20yaz1biM2MWXyi7HAcI0pb-BHYDYD1XM92Al11dQPQ26OJY8YULAlHPHtduGETCN5Y5D6aXtkiFi3-9tB3RNtj4A687SGo765evyqri2TjKMCyQeNSLNfZ-SV52yXlIEar9iQj2aEzPKAmBGrQOA=w628-h449-no

Todo Explain:

- make monitor
- make debug
- memory mapped hardware registers.
- reset vector

Program code

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

gdb tui

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eVGqrh2Gm1lQJKH27cWNYUQO8fVTUAvM1FNZ_pUis0Upip6vEa4ZNGOh79vosxGnBtFcacVX8QRNDgKEeklwFnI9hs6WrAlnzpTDZIyyn1oyTclXxU4_IlzydFbb0UFDkm0CFMsU8f3KIEKY0OWxoPzQ=w354-h710-no

Miro Samek and the modern embedded course series
================================================
I will be loosing cloning MIROS following some of his videos in spirit. He does a great introduction to many concepts in embedded and I want to share that in a way that we don't need to have a real board.
