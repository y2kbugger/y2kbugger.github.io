MMIX - Why I am working on TAOCP in RISC
########################################

:date: 2018-12-27 00:00:00
:modified: 2020-05-18 13:14:09
:tags: assembly, algorithms, MMIX, TAOCP, books
:author: zak kohler
:summary: After getting The Art of Computer Programming for Christmas, I had to decide: "MIX or MMIX?"
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17


The Art Of Computer Programming
===============================
The Art of Computer Programming is about as legendary as computer science books get. The goal was to describe and teach a wide range of algoritms. Originally concieved in 1962 as a single book with 12 chapter, rapid advancements being made in the field caused a content expansion that continues today-volume one was released in 1968, and volume 4 is still in progress.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fz2RxP2aYWm20KIl9hU_BkQcyTNxSmewF-0TM7KLe2BbVwUsml4DmX7kgHf4E8vARaOSQFJ-d1zou3FMoD4hjaX8q3jSFcKZwty559C8BiomechHmEW7gwmIBd8kJvi0u4Zqx0I6UDlA65QuBUX_CEdQ=w500-h431-no
   :width: 33%
   :alt: The art of Computer Programming
   :align: center

The book is notable for it's precision and accuracy as well as extreme care given to the exercises and solutions. It is also sometimes accused of being a book that people recommends but which . This might be due to the fact that all of the book is taught using assembly language rather than structured programming. [#taocpwiki]_

Why I want to read it
---------------------
I believe it when Knuth says that you learn something more about algorithms at the interface of hardware and software. In C for example you may not know what is happening in hardware when you write an if statement, but in assembly this becomes explicit.

He puts it like this [#knuthmmix]_:

    One of the principal goals of my books is to show how high-level constructions are actually implemented in machines, not simply to show how they are applied.

This is aligned with my goal to explore the parts of computing that might typically be ignored by many programmers. The more I can understand the software-hardware interface, the happier I will be. Learning algorithms via TAOCP is the software side of my strategy, for hardware I'm exploring TTL series logic and CPU design as well as simple cases of systems integration using vintage microcontrollers. This has also led me to exploring prototyping via FPGA and one day I hope to design a CPU core and bootstrap up to a self hosting multitasking development environment.

MIX
===
In order to facilitate the teaching of algorithms and how they interact with hardware he has developed a CPU architecture and assembly languages.

Wikipedia [#mixwiki]_:

    MIX is a hypothetical computer used in Donald Knuth's monograph, The Art of
    Computer Programming (TAOCP). MIX's model number is 1009, which was derived
    by combining the model numbers and names of several contemporaneous,
    commercial machines deemed significant by the author. Also, "MIX" read as a
    Roman numeral is 1009.

Knuth states that "MIX is very much like nearly every computer of the 1960s and 1970s except that it is, perhaps, nicer."

MMIX
====
.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no
   :alt: MMIX

Knuth states in the third edition of his book:

    However, it must be admitted that MIX is now quite obsolete. Therefore MIX will be replaced in subsequent editions of this book by a new machine called MMIX, the 2009. MMIX will be a so-called reduced instruction set computer (RISC). [...] It will be even nicer than MIX and will be similar to machines that have become dominant during the 1990s.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fRUt39VqJiEOQ9LhFcwVrsuth55pRA44lyfN51vxoNG0v0DshXSPqc5SdCtLdAnCWPOfLaP-KS5iDdApF0YKfAM8SBZmgyI61tLobpe8lVmxjGyNFkdrOpxaOD4cpvrJddWkV7lvJAUvmMONAoJF6dtg=w683-h131-no

Knuth [#knuthmmix]_:

    Thirty years have passed since the MIX computer was designed, and computer architecture has been converging during those years towards a rather different style of machine.

Subsequent editions, fascicles
==============================
So we've chosen the path towards the future, now what? The dilemma we face is that the next edition has not been released yet. The currently available version of the book has all questions and answers is still all written with MIX.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cuRVuJCUSUugDBBPjEjvV-g4h9rh4NuHipmWhjvJbgS3zKZGBYrkea6kFi6MYL6-gC-mmhqHvCIB6FMcG6fHf_wzLQ3FSggliRMHXReoaJXcB4XEkEYYUFVJ-tzUwnb0Htv9v26hcMSSMf6vrfC46HXQ=w683-h459-no
   :alt: The three required books for MMIX
   :align: center

So what choice do we have then? Well Donald has kindly release what is known as V1F1 or *The Art of Computer Programming, Volume 1, Fasicle 1 -- A RISC Computer for the New Millennium*. A fascicle is a "a separately published installment of a book or other printed work." Basically it acts as a patch for V1 3e. Replacing the chapter explaining MIX with the MMIX equivalent. It is available on `Amazon <https://https://www.amazon.com/Art-Computer-Programming-Fascicle-Millennium/dp/0201853922/>`_.

That covers the basics of the language, but all of the solutions also needed reworked. Knuth put out a request for people to get together and create the solution [#mmixmasters]_. The end result of this is known as the MMIX supplement. It's available on the web, http://mmix.cs.hm.edu/supplement/index.html as well as in printed from on Amazon: `MMIX Supplement <https://www.amazon.com/MMIX-Supplement-Computer-Programming-Volumes/dp/0133992314>`_.

Hardware and RISC-V
===================
I'm excited to start working through exercises these exercises. At the same time I plan to continue working on the hardware side as well and I dream of the day I could some of the algorithms running on a RISC-V cpu or even more exciting, a toy ISA of my own.

.. [#taocpwiki] https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming
.. [#mixwiki] https://en.wikipedia.org/wiki/MIX
.. [#knuthmmix] https://www-cs-faculty.stanford.edu/~knuth/mmix.html
.. [#mmixmasters] http://mmix.cs.hm.edu/mmixmasters/index.html
