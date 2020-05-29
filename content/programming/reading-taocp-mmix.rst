MMIX - Working on TAOCP in RISC
###############################

:date: 2018-12-27 00:00:00
:modified: 2020-05-29 15:18:21
:tags: assembly, algorithms, MMIX, TAOCP, books
:author: zak kohler
:summary: How to read The Art of Computer Programming and do the exercises in modern RISC rather than a 1960s style architecture.
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

Introduction
============
This article I will cover why I want to read TAOCP as well as my approach. Because the books are in various states of publication, one must use additional resources besides the book to enjoy the updated RISC material.

The Art Of Computer Programming
===============================
The Art of Computer Programming is a legendary multi-volume computer science textbook. It was originally conceived in 1962 as a 12 chapter book documenting a wide range of algorithms. The rapid pace of change in computer science made these chapters a moving target; while Volume 1 was released in 1968, Volume 4 is still in progress as of 2020 [#taocpwiki]_.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fz2RxP2aYWm20KIl9hU_BkQcyTNxSmewF-0TM7KLe2BbVwUsml4DmX7kgHf4E8vARaOSQFJ-d1zou3FMoD4hjaX8q3jSFcKZwty559C8BiomechHmEW7gwmIBd8kJvi0u4Zqx0I6UDlA65QuBUX_CEdQ=w500-h431-no
   :width: 33%
   :alt: The Art of Computer Programming
   :align: center

The book is notable for being comprehensive and precise as well as for the extreme care given to the exercises and solutions. Because it known for being a huge undertaking, some people quip that the book is often recommended without actually having been read. I suspect this is be the algorithms are explained using assembly language rather than structured programming which some people deem as impenetrably  obscure.

Why I want to read it
---------------------
I believe it when Knuth says that you learn something extra about algorithms at the interface of hardware and software. In C for example you may not know what is happening in hardware when you write an if statement, but in assembly this is in-your-face.

He puts it like this:

    One of the principal goals of my books is to show how high-level constructions are actually implemented in machines, not simply to show how they are applied. [#knuthmmix]_


This aligns with my goal of exploring computers to the lowest levels including operating systems as well as CPUs. The more I can understand the software-hardware interface, the happier I will be. Learning algorithms via TAOCP is the software side of my strategy. On the hardware side I'm exploring TTL logic, CPU design, and simple cases of systems integration using vintage microprocessors such as z80, 6502 and 1802. This has also led me to explore prototyping via FPGAs and one day I hope to design a CPU core and bootstrap up to a self hosting multitasking development environment.

MIX
===
In order to facilitate the teaching of algorithms and how they interact with hardware, Knuth developed a CPU architecture and corresponding assembly language.

    MIX is a hypothetical computer used in Donald Knuth's monograph, The Art of
    Computer Programming (TAOCP). MIX's model number is 1009, which was derived
    by combining the model numbers and names of several contemporaneous,
    commercial machines deemed significant by the author. Also, "MIX" read as a
    Roman numeral is 1009.

    -- Wikipedia [#mixwiki]_

Knuth states that "MIX is very much like nearly every computer of the 1960s and 1970s except that it is, perhaps, nicer."

MMIX
====
.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no
   :alt: MMIX

Computer have changed significantly since the 60s, as Knuth explains:

    Thirty years have passed since the MIX computer was designed, and computer architecture has been converging during those years towards a rather different style of machine [#knuthmmix]_.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fRUt39VqJiEOQ9LhFcwVrsuth55pRA44lyfN51vxoNG0v0DshXSPqc5SdCtLdAnCWPOfLaP-KS5iDdApF0YKfAM8SBZmgyI61tLobpe8lVmxjGyNFkdrOpxaOD4cpvrJddWkV7lvJAUvmMONAoJF6dtg=w683-h131-no
   :alt: Under Construction

In Volume 1 3rd Edition, he states his plans to replace MIX:

    However, it must be admitted that MIX is now quite obsolete. Therefore MIX will be replaced in subsequent editions of this book by a new machine called MMIX, the 2009. MMIX will be a so-called reduced instruction set computer (RISC). [...] It will be even nicer than MIX and will be similar to machines that have become dominant during the 1990s.


Subsequent editions, fascicles
==============================
So we've chosen MMIX, the path towards the future, now what? The dilemma we face is that the next edition has not been released yet. The most recent edition, V1 3e, has all of the questions and answers still written with MIX.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cuRVuJCUSUugDBBPjEjvV-g4h9rh4NuHipmWhjvJbgS3zKZGBYrkea6kFi6MYL6-gC-mmhqHvCIB6FMcG6fHf_wzLQ3FSggliRMHXReoaJXcB4XEkEYYUFVJ-tzUwnb0Htv9v26hcMSSMf6vrfC46HXQ=w683-h459-no
   :alt: The three required books for MMIX
   :align: center

So what choice do we have then? Well Donald has kindly release what is known as V1F1 or *The Art of Computer Programming, Volume 1, Fasicle 1 -- A RISC Computer for the New Millennium*. A fascicle is a "a separately published installment of a book or other printed work." Basically it acts as a patch for V1 3e. Replacing the chapter explaining MIX with the MMIX equivalent. It is available on `Amazon <https://https://www.amazon.com/Art-Computer-Programming-Fascicle-Millennium/dp/0201853922/>`_. Fun note, these are printed on demand when you place your order.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3dsG1EowkXAZFHTN5U6GoiV7aHLiLZj4qS4T-LL4_G7bSkTLQFbru0xIrfOSHiVYxg3UDcSqjI3_DC0HQvAiMNwwaaUBNkcFkEqL0Zx5m11fvY5ctohhCmg8e60Y_SAX8k1jyvou9g_R2JqBcRycjhmbg=w509-h678-no
   :width: 66%
   :alt: On demand printing
   :align: right

   Printed the day after I ordered on Amazon.

That covers the basics of the language, but all of the solutions also needed reworked. Knuth put out a request for people to collaborate on the solutions, a project he called MMIXMasters [#mmixmasters]_. The end result of this is known as the MMIX supplement. It's available on the web, http://mmix.cs.hm.edu/supplement/index.html as well as in printed form on Amazon: `MMIX Supplement <https://www.amazon.com/MMIX-Supplement-Computer-Programming-Volumes/dp/0133992314>`_.

Future Work
===========
I'm excited to keep working through these exercises. To assist the process of testing various algorithms, I've started a side-project which I have compiled Knuth's original MMIX toolchain to WASM and wrapped it in a simple IDE for MMIX in the browser.

Hardware and RISC-V
===================
I plan to continue working on the hardware side in tandem as well. I dream of the day I could write some of these algorithms for an FPGA RISC-V CPU or even more exciting, a toy ISA of my own.

.. [#taocpwiki] https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming
.. [#mixwiki] https://en.wikipedia.org/wiki/MIX
.. [#knuthmmix] https://www-cs-faculty.stanford.edu/~knuth/mmix.html
.. [#mmixmasters] http://mmix.cs.hm.edu/mmixmasters/index.html
