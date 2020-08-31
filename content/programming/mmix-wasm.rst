MMIX WASM
##########

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
MMIXware is made up of an assembler, and a simulator. Details can be found at the homepage here: http://mmix.cs.hm.edu. When browsing the SVN trunk I noticed something called MMIXlib. This is a refactoring effort by Martin Ruckert to partition the original MMIX tools into something he could integrate into an IDE. I decided to use this as the base for how I would plug into the MMIX assembler and simulator.

One thing that is surprising if you haven't seen it before is that MMIXware is written in CWEB, the literate programming system developed by Donald Knuth. The WEB files compile to C, but I needed to install all of texlive to do so.

When I was working through the compilation process, I found a couple of errors, and also I suggested a small enhancement to the Makefile for mmixlib. As is tradition with Donald Knuth projects, there is a reward for finding errors. Even though I think my contribution was small i'm proud to have gotten a cool MMIX shirt.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3ezdKEXl-Hb4fRD5jeCqHH2lObD7xjwU3zH2j9jQC3-O-Cd01Cubl6hFdAh3sYxz-kZ52qdDVVwsUSYNmcNBJ-S3tcBbPp2a_NkfXnbZh97fpfgewD7SF1I0RrLHS-uzDrbDsb8NzhqfS2EcLJDBGWKrg=w471-h628-no

Emscripten
----------
I decided to compile to WASM for two reasons:
I decided to try to compile parts of MMIX to web assembly.

 - I wanted to see what it took to compile some legacy C program to WASM
 - The web is a flexible for UIs, I could make it as polished as I wanted

Demo
====

.. code-block:: giturl

   git clone git@github.com:y2kbugger/mmix-wasm.git

Before publishing this:

 - label "error", input and output text areas
 - clean up example program
 - recompile with unsigned int fix

.. raw:: html

    <iframe frameborder="0" width="100%" height="1200px"  src="http://mmix.y2kbugger.com.s3-website.us-east-2.amazonaws.com"></iframe>

