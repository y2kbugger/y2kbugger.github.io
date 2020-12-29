Baremetal RISC-V Renode - Part 2: Toolchain considerations
##########################################################

:date: 2020-12-22 00:11:42
:modified: 2020-12-22 00:11:42
:tags: baremetal, RISC-V, Renode, assembly, CPUs
:author: zak kohler
:summary: A quick review of different simulators and toolchains that I have tried or heard about.
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3fN25durhdecjcr3ylVSbYMFnkAjgCjz9Gcx3W0Z55FvTu6UQTN8Pb6CyXEixflzo6G5k5OjIWySt9m8zAjagYwheB16dRUSLVQ7p651kNjxK8v1emUVd1yD5FwRN9H7MJJuLMYgypQdNoTZ9fHPAIedA=w442-h197-no`

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78
  https://www.youtube.com/watch?v=D0VuYe77Wu0&list=PLb-MsRpo_wlLW0EWRpAqnbbDsf4kxSI1x

.. contents::
    :depth: 2

Background
==========

I'm exploring the line between hardware and software by creating a series of demos within a minimal, free and open source environment. These demos span from blinking an LED to implementing a toy operating system. The goal is to minimize parts of the system that we take for granted and gain a better understanding of computers and operating systems.

Start at `Part 1 <{filename}/programming/baremetal-riscv-renode-1.rst>`_, We give a bare minimum example to setup toolchains, blink a virtual LED, and debug the software in real-time using GDB.

Compiler toolchains
===================
In part one we set up a cross compiling GDB.

As of September 2019, LLVM 9 has an promoted the *experimental* RISC-V backend to *official*. The support has been prototyped as `lowRISC` starting in 2016, which was then merged upstream as *experimental* before being promoted to *official* This history indicates that there has probably been considerable testing


Simulators
==========
Renode
Qemu


Integrated Development environments
===================================
platformio (VSCODE)
litex buildenv
eclipse (CDT)
VSCODE + (myriid of debugging integrations)

(understaning how the openOCD debugger interface works for renode, compare to segger/jlink, etc))
IAR
Segger
https://www.sam-solutions.com/blog/top-ten-embedded-software-development-tools/



Operating systems/SDK
===================================
Zephyr https://www.zephyrproject.org/zephyr-an-operating-system-for-iot/
Linux
FreeRTOS
efreedomsdk
MBed OS
NuttX
https://micro-ros.github.io/docs/concepts/rtos/comparison/


Next post
=========

Footnotes
=========
.. [#dddddd] The computer 
