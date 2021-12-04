Baremetal RISC-V Renode - Part 2: Tool considerations
#####################################################

:date: 2021-01-03 23:55:43
:modified: 2021-01-22 23:55:43
:tags: baremetal, RISC-V, Renode, assembly, CPUs
:author: zak kohler
:summary: A quick review of different simulators and toolchains that I have tried or heard about.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3fN25durhdecjcr3ylVSbYMFnkAjgCjz9Gcx3W0Z55FvTu6UQTN8Pb6CyXEixflzo6G5k5OjIWySt9m8zAjagYwheB16dRUSLVQ7p651kNjxK8v1emUVd1yD5FwRN9H7MJJuLMYgypQdNoTZ9fHPAIedA=w442-h197-no`

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78
  https://www.youtube.com/watch?v=D0VuYe77Wu0&list=PLb-MsRpo_wlLW0EWRpAqnbbDsf4kxSI1x

.. contents::
    :depth: 2

Baremetal RISC-V Renode Series
==============================
I'm exploring the line between hardware and software by creating a series of demos within a minimal, free and open source environment. These demos span from blinking an LED to implementing a toy operating system. The goal is to minimize parts of the system that we take for granted and gain a better understanding of computers and operating systems.

Start at `Part 1 <{filename}/programming/baremetal-riscv-renode-1.rst>`_, we setup a bare minimum LED blinking example to demonstrate how to compile your development environment and debug the software in real-time using GDB.

Background
==========
This post catalogs the tools I tried as well as the tools I skipped over when developing the dev environment from Part 1. Comment below if I missed something or if something new has come out.

Compiler toolchains
===================
As stated in part one, because one goal is to run RISC-V binaries, we need a compiler that can run on an x86 PC, but compile to RISC-V bytecode.

GCC
---
In `Part 1 <{filename}/programming/baremetal-riscv-renode-1.rst>`_ we set up a RISC-V cross compiling GCC. To me, riscv-gnu-toolchain seemed to be the official C compiler for RISCV. Many other SDKs/IDEs are based on the gcc as well.

I use riscv-gnu-toolchain instead of upstream gcc because it includes binutils and C library build configurations.

LLVM/Clang
----------
As of September 2019, LLVM 9 has promoted the *experimental* RISC-V backend to *official*. The support has been prototyped as `lowRISC` starting in 2016, which was then merged upstream as *experimental* before being promoted to *official*. This history indicates that there has probably been considerable testing, comment if you know of any production applications.

LLVM has some features/warnings that GCC might be missing. It may also integrate with code analysis tools and autocompletion in a more streamlined way.

One other thing I find interesting is that the main author of LLVM, Chris Lattner, has been `hired by the RISC-V company SiFive <https://www.sifive.com/blog/with-sifive-we-can-change-the-world>`_.

Simulators/Emulators
====================
In order to run non-native code, we need a simulator. This can be as simple as just translating the from one ISA to another, but it can also include peripherals and OS functionality, such as standard input output.

Renode
------
I learned of Renode from the FPGA community. From what I can tell, they are able  high level hardware description language and compile it to either an FPGA bitstream or a Renode platform. This allows simulating an entire system, hardware and software together, without ever needing physical hardware and therefore, easier and more complete automatic testing.

Qemu
----
Qemu a very popular emulation and virtualization tool. It is very useful for running non-native binaries within linux. Others use it for running guest operating systems. When I spent some time with it, I couldn't control the low-level details of the platform as much as Renode. A lot of complexity in the system seemed to revolve around PC peripherals, GUI, and virtualization that doesn't matter for trying to learn about baremetal programming. I also couldn't figure out a way to get rid of PC BIOS.

Spike
-----
Spike is a RISC-V specific emulator: https://github.com/riscv/riscv-isa-sim

I haven't tried this one myself. I looks like configurability is focused on customizing the CPU, e.g. custom opcodes, rather than IO or other embedded hardware.

Educational
-----------
Below are a few graphical simulators that try to explain the execution as it is happening. These are targeted at understanding opcodes and other RISC-V specifics rather than actually programming for a hardware platform with peripherals.

- http://tice.sea.eseo.fr/riscv/
- https://ascslab.org/research/briscv/simulator/simulator.html


Integrated Development environments
===================================
There are many good IDE solutions if your goal get work done on an embedded application, I discuss a few in detail below.

These IDEs provide standard development tools such as compiler and debugger, but also support deploying to a board for testing and debugging on a board via JTAG or other hardware debugger.

Some even support deploying to a simulator rather than real-work target. To me this is very valuable as it enables testing automation without requiring specific hardware.

Eclipse CDT
-----------
After figuring out the Java runtime and getting the versions of Eclipse and the CDT extension all working, I kinda ran out steam as every configuration was overly "eclipse centric". I wanted to spend my time learning about embedded not learning about eclipse.

Platformio
----------
Platformio is a universal embedded development extension for Microsoft's VS Code.

Platformio describes itself as:

    Open source, cross-platform IDE and Unified Debugger. Static Code Analyzer and Remote Unit Testing. Multi-platform and Multi-architecture Build System.

I found that it was super convenient for "just getting starting" and getting stuff done. It is heavy but the extension bootstraps itself and the defaults are very sane. However, like eclipse, I didn't want to spend my time learning "how does Platformio work" every time I want to peek behind the curtain or tweak something low-level.

Additionally, it only supported a handful of real boards when integrating with Renode, and it wasn't straightforward on how to customize the Renode platform and keep the integration working.

Lastly, since it is a VS Code extension, we don't have a way to reproducibly build the platform and therefore any blog I write could go outdated as Platformio evolves.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3eEUNqaGzfNKQxydmtODWEllXemhHGT0fzswHlEIpK1-o6kQRy-xxHL1m7rXy64cLI5j_JHbVO4oqtAif-M9_Hn8XCUCGBlf6dCj-eDa-T7O2RWrMZZ86d-NbUUlHxEnBg3XXIWZUalZfbfj-oYOsRHIQ=w960-h494-no
   :alt: Platformio screenshot

   Using Platformio to interact with registers, memory, source code and disassembly.

VS Code
-------
I also tried to configure a handful different VS Code extensions to support our manually compiled GCC cross compiling toolchains. None ever ended up with better GDB support than the native GDB TUI. The three most promising were:

- `C/C++ for Visual Studio Code <https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools>`_ - Microsoft's official C extension. Configurable but not configurable enough.
- `Native Debugger <https://marketplace.visualstudio.com/items?itemName=webfreak.debug>`_ - This one seems like it could work, but I don't think I ever got it launching/debugging how I wanted it. It's open source so I think it could be done, even if it required more than just configuration.
- `Cortex-Debug` <https://marketplace.visualstudio.com/items?itemName=marus25.cortex-debug>`_ Another open source extension. Although it is ARM specific, you provide your own gnu toolchain, so it may be viable.

litex buildenv
--------------
https://github.com/timvideos/litex-buildenv

Litex buildenv is much more than just a way to compile code and get it running on real or simulated hardware. It actually facilitates specifying hardware in high level hardware description languages and compiling that down to create a soft CPU core on an FPGA. As part of the environment, it can be configured to deploy software to either a renode simulator, or to actual hardware.

Other
-----
- IAR
- Segger
- https://www.sam-solutions.com/blog/top-ten-embedded-software-development-tools/


Operating systems/SDK
===================================
- freedom e sdk - https://github.com/sifive/freedom-e-sdk This SDK is totally worth reading through and trying. You will learn a lot.
- Zephyr https://www.zephyrproject.org/zephyr-an-operating-system-for-iot/
- Linux
- FreeRTOS
- MBed OS
- NuttX
- https://micro-ros.github.io/docs/concepts/rtos/comparison/

Next post
=========
In the next post I will show how to do basic IO via Serial UART. This introduces how to utilize hardware interrupts and how to compile C along with the RISC-V assembly.
