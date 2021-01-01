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

GCC
---
In `Part 1 <{filename}/programming/baremetal-riscv-renode-1.rst>`_ we set up a RISC-V cross compiling GCC. To me, riscv-gnu-toolchain seemed to be the official C compiler for RISCV. Many other SDKs/IDEs are based on the gcc as well.

I use riscv-gnu-toolchain instead of upstream gcc because it includes binutils and C library build configurations.

LLVM/Clang
----------
As of September 2019, LLVM 9 has an promoted the *experimental* RISC-V backend to *official*. The support has been prototyped as `lowRISC` starting in 2016, which was then merged upstream as *experimental* before being promoted to *official* This history indicates that there has probably been considerable testing
LLVM has some features/warnings that GCC might be missing. It may also integrate with code analysis tools and autocompletion in a more streamlined way.
One other thing I find interesting is that the main author of LLVM, Chris Lattner, has been `hired by the RISC-V company SiFive <https://www.sifive.com/blog/with-sifive-we-can-change-the-world>`_.

Simulators/Emulators
====================

Renode
------
I learned of Renode from the FPGA community. They are actually close (or maybe already done) to being able to take a high level hardware description and compile it to either an FPGA bitstream or a Renode platform. This allows simulating an entire system, hardware and software together, without ever needing physical hardware. This allow for easier and more complete automatic testing.

Qemu
----
This a very popular emulation and virualization tool. Seems very useful for running non-native binaries within linux. Others use it for running guest operating systems. When I spent some time with it, I couldn't control the low-level details of the platform as much as Renode, and a lot complexity in the system seemed to revolve around PC peripherals, GUI, and Virtualization that doesn't matter for trying to learning about baremetal. I also couldn't figure out a way to get rid of PC BIOS.

Spike
-----
Found this one with a quick google search: https://github.com/riscv/riscv-isa-sim. I looks like configurability is focused customizing the CPU, e.g. custom opcodes, rather than IO or other embedded hardware.

Educational
-----------
These are a few graphical simulators that try to explain the execution as it is happening. These are targeted at understanding opcodes and other RISC-V specifics rather than actually programming for a hardware platform with peripherals.

- http://tice.sea.eseo.fr/riscv/
- https://ascslab.org/research/briscv/simulator/simulator.html


Integrated Development environments
===================================

(understaning how the openOCD debugger interface works for renode, compare to segger/jlink, etc))

Eclipse CDT
-----------
After figuring out java runtime and trying to get started, I kinda ran out motivation when every configuration was overly "eclipse centric". I want to spend my time learning about embedded not about eclipse.

Platformio
----------

Platformio describes itself as:

    Open source, cross-platform IDE and Unified Debugger. Static Code Analyzer and Remote Unit Testing. Multi-platform and Multi-architecture Build System.

I found that it was super convenient for "just getting starting" and getting stuff done. It is really heavy and, like eclipse, I didn't want to spend my time learning "how does platformio work" every time I want to peek behind the curtain or tweak something low-level.
Additionally, it only supports a handful of real boards when integrating with Renode, and it wasn't straightforward on how to customize the renode platform and keep the integration working.

Lastly, since it is a VS Code extension, we don't have a way to reproducibly build the platform and therefore any blog I right could go outdated as Platformio evolves.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3eEUNqaGzfNKQxydmtODWEllXemhHGT0fzswHlEIpK1-o6kQRy-xxHL1m7rXy64cLI5j_JHbVO4oqtAif-M9_Hn8XCUCGBlf6dCj-eDa-T7O2RWrMZZ86d-NbUUlHxEnBg3XXIWZUalZfbfj-oYOsRHIQ=w960-h494-no
   :alt: Platformio screenshot

   Using Platformio to interact with registers, memory, source code and disassembly.


VSCODE (Custom)
---------------
(myriid of debugging integrations)

litex buildenv
--------------


Other
-----
- IAR
- Segger
- https://www.sam-solutions.com/blog/top-ten-embedded-software-development-tools/



Operating systems/SDK
===================================
- Zephyr https://www.zephyrproject.org/zephyr-an-operating-system-for-iot/
- Linux
- FreeRTOS
- efreedomsdk
- MBed OS
- NuttX
- https://micro-ros.github.io/docs/concepts/rtos/comparison/


Next post
=========
In the next post I will show how to do basic IO via Serial UART. This introduces how to utilize hardware interuptt and how to C along with the RISC-V assembly.

Footnotes
=========
.. [#dddddd] The computer.
