MMIX, WASM, What?
#################

:date: 2018-03-04
:modified: 2020-05-18 13:14:09
:tags: assembly, algorithms, MMIX, TAOCP, books
:author: zak kohler
:summary: Compiling the MMIX Assembler and Simulator to Web Assembly
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

Fast feedback for The Art of Computer Programming Exercises
===========================================================
As a started working through the `exercises in TAOCP <https://blog.y2kbugger.com/reading-taocp-mmix.html>`_, I wanted a quicker way to work on the problems in assembly language. I was also in the process of learning C so I was interested in trying to understand the code behind MMIXware, the simulators for the MMIX computer.


Dependencies
============

MMIXlib
-------
MMIXware is made up of an assembler, and a simulator. Details can be found at the homepage here: http://mmix.cs.hm.edu. One thing I noticed while browsing the SVN trunk was MMIXlib. This is a refactoring of the original MMIX tools for integrating into an ide. I decided to use this as the base for how I would plug into the MMIX assembler and simulator.

The first issue you'll run into is that MMIXware is written in CWEB, the literate programming system developed by Donald Knuth. The WEB files compile to C, but you'll likely need to install all of texlive to do so.

***problem with make file
***Show shirt

Emscripten
----------
Since the web is a killer UI framework, and I also wanted to see what it took to compile some legacy C program to WASM, I decided to try to compile parts of MMIX to web assembly.


My little REPL
==============

.. code-block:: giturl

   git clone git@github.com:y2kbugger/mmix-wasm.git

Give an example string processing version of program.

embed the demo here

