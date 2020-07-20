The C Programming Language
##########################

:date: 2019-12-31 00:00:00
:modified: 2020-07-19 22:54:03
:tags: C, books
:author: zak kohler
:summary: Learning C from the book written by the original language designer.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3eFvejBEI9Qmr_scx1xpuCPMU_1BLAgQ5fxIjrCo0jmv0EnmVyIjUTE2WYtA0sd0aV6oCpb2TIG7xj35pttUYfxmq8fJzAQMEcY1F5Pivo8dOECxbql-qYTUHFIYL8LClxwZNONGlPwkeTvV8mZnv8x4g=w362-h479-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

Get close to the hardware so you can C
======================================
Since I have been learning about hardware and operating systems I wanted to learn a language which is conducive for having full control of computer hardware. C is not just good for this, the level of control C gives you was tuned for writing portable operating systems. The tooling, community, and educational resources reflect this legacy.

I chose to read the Kernighan and Ritchie book because I had heard that it was not just a good book for C, but good for programming in general. There is also a historical value to learning from a primary source. I can confirm this. Working through the exercises are key to understanding why C exists.

Here are my attempts at the exercises:

.. code-block:: giturl

   git clone git@github.com:y2kbugger/kr.git

The K&R approach
----------------
Early on they teach about structuring modules so that code and interfaces could be reused. When I previously learning C++ the reason for header files seemed to be hand waved. I appreciated the way these concepts were treated in K&R.

Later in the book though we work through reimplement functions from the standard lib. This was insightful, especially the ones which dealt with memory management such as malloc, calloc, and free as well as the Unix system interface.

Conclusion
----------
I would definitely recommend the book to anyone interested in learning about computers. If all you care about is writing programs/computation, other languages could twist you brain in other directions (Haskell, etc), but learning C through K&R is a good start to learning about how computers actually work.

But shouldn't I learn something modern like C++?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As a side note, don't be swayed to learn C++ merely because C is a subset. The argument goes like this: if you learn C++ you'll also learn C for free. This isn't true. If you want something a bit higher level for systems programming, I've heard good things about Rust.
