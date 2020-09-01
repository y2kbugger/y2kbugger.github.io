MMIX WASM
##########

:date: 2019-09-28 02:14:30
:modified: 2020-09-01 02:32:27
:tags: assembly, algorithms, MMIX, TAOCP, books
:author: zak kohler
:summary: Compiling the MMIX Assembler and Simulator to Web Assembly
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cFCw5pcP4PjQ42htLHTNWtHNCmNJq4lxvQjEMtxlMtKjBK_P6DHh2c05aIIGVsdb5RBNnMFY7dOzUsMa8EECwxEvNJY8tTF4hpSk00R7sk52YwUXK55kyJkIC9epT5yxHK_k8DqhKY6qrrMXL1YOaC3Q=w742-h989-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

.. contents::

Fast feedback for The Art of Computer Programming Exercises
===========================================================
As I started working through the `exercises in TAOCP <https://blog.y2kbugger.com/reading-taocp-mmix.html>`_, I wanted a quicker way to work on the problems in the MMIX assembly language. I was also in the process of learning C so I was interested in trying to understand the code behind MMIXware, the simulators for the MMIX computer.


Dependencies
============

MMIXlib
-------
MMIXware is made up of multiple programs, including an assembler and a simulator. Details can be found at the homepage here: http://mmix.cs.hm.edu. When browsing the SVN trunk I noticed a project called MMIXlib. This is a refactoring effort by Martin Ruckert to partition the original MMIX tools into something he could integrate into an IDE. I decided to use this as the base for how I would plug into the MMIX assembler and simulator.

One thing that is surprising if you haven't seen it before is MMIXware being written in CWEB, This is a literate programming system developed by Donald Knuth. The CWEB files compile to C, but I needed to install all of texlive to do so. There is a rule that you are not to change the original source code but only apply CWEB style "change files". This allows the entire refactoring to actually be a layer of explained changes applied to the original MMIXware.

When I was working through the compilation process, I found a couple of errors in MMIXlib, and also I suggested a small enhancement to the Makefile. As is tradition with Donald Knuth's projects, there was a reward for finding errors in MMIXware. Even though I think my contribution was small I'm proud to have gotten a MMIX shirt for the contribution.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cFCw5pcP4PjQ42htLHTNWtHNCmNJq4lxvQjEMtxlMtKjBK_P6DHh2c05aIIGVsdb5RBNnMFY7dOzUsMa8EECwxEvNJY8tTF4hpSk00R7sk52YwUXK55kyJkIC9epT5yxHK_k8DqhKY6qrrMXL1YOaC3Q=w742-h989-no

Emscripten
----------
I decided to compile to MMIXware to web assembly for two reasons:

1. I wanted to see what it took to compile some legacy C program to WASM
2. The web is flexible for UIs, I could make it as polished as I wanted

Approach
========
MMIXlib allows you to hook into various parts of the simulator and emscripten allows exposing C functions directly to JavaScript. This allows the main loop to run in js, with all of the hard work being done on the WASM side. Emscripten also has the ability to fake out a file system and expose that to JavaScript as well. This allowed me to be extra lazy and not even have to modify the IO of MMIXware.

The hardest part was deciphering compile errors/warnings that manifested from compiling old C code with a modern compiler while also tracing through CWEB source and change files.

The part that I can take the most credit for is adding the register watcher. This involved work on both the js side and the C code. I hope to add the ability for watching multiple registers. Other inner workings I would like to expose are special registers and memory ranges.

Demo
====
As you modify the input, the simulator will reassemble and restart. Choose a general register to watch, 0-255. You can also change the frequency we run the simulator at.

More programming examples can be found in the MMIX repository https://gitlab.lrz.de/mmix/mmixware.

.. code-block:: giturl

   git clone git@github.com:y2kbugger/mmix-wasm.git

.. raw:: html

    <iframe frameborder="0" width="100%" height="1400px"  src="https://d1aby3vgncc46a.cloudfront.net/mmix-wasm.html"></iframe>

