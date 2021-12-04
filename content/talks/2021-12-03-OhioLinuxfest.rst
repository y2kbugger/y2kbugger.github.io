A Simple RISC-V Multitasking OS for Learning
############################################

:date: 2021-12-03
:modified: 2021-12-03
:tags: Ohio Linuxfest, baremetal, RISC-V, Renode, assembly, CPUs
:author: zak kohler
:summary: Ohio Linuxfest 2021, Columbus, Ohio
:cover: `https://lh3.googleusercontent.com/pw/AM-JKLU9BztvQWGFhPc8Mhn69mu8jLb0waOp_AYkSeul65l4NexXCSMzrgrmGFbdCTnKo3k3eQZt1k1pfv1i7ZpX7lPCHzJ2eIMFhfaTchvNH2r_Nus9buX0LylyLB9MfCv4HeH7mUcosliRYjONdbemYxrVtw=w893-h501-no`
:status: published

@ **Ohio Linuxfest**, *Columbus, Ohio*

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

`Slides <https://docs.google.com/presentation/d/1BQ1FQoe7_6b0b84McHxIMIjrNTbw7o7dNMAjr6hmTFw/edit?usp=sharing>`_

`Blog Article (coming soon) <{filename}/programming/baremetal-riscv-renode-4.rst>`_

.. code-block:: giturl

   git clone https://github.com/y2kbugger/baremetal-riscv-renode.git


.. raw:: html

    <div class="videoembed-container">
    Youtube embed coming soon
    <!-- <iframe class="videoembed-iframe" src="https://www.youtube.com/embed/JkeRezvCVfM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>--!>
    </div>


Abstract
========
Explore the line between hardware and software by writing code with absolute control over the cpu and peripherals. We'll explore how to do this using a completely free and open source simulator (Renode), toolchain (GCC), and instruction set (RISC-V). Using assembly, we'll initialize parts of the system such as CPU interrupts and privilege levels. Finally we'll review the assembly code for doing a context switch, the key software to which enables multitasking via timesharing.

Bio
===
Zak Kohler is a Chemical Engineer by training but a hacker at heart. He started programming in 3rd grade and has never let up. His first foray in open source was in early high school, and he discovered Linux and Free Software at university. Electronics is his second love and he fuses the two by playing with early computer hardware, modern microcontrollers and FPGAs. When zak isn't messing with computers he can be found growing plants, drawing, and exploring the world on foot.


