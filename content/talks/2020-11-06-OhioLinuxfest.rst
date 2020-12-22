Baremetal RISC-V Renode
#######################

:date: 2020-11-06
:modified: 2020-11-06
:tags: Ohio Linuxfest, baremetal, RISC-V, Renode, assembly, CPUs
:author: zak kohler
:summary: Ohio Linuxfest 2020, Virtual
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3fTB1LkFo46llCKGgulxWISEd4Zgl1PYIxxgWs3G9-7Y066QGthphrKyyol1XWuLFGSB87o8O4xFLejO-0CvLRUsXJpT-ERFGPPC0AB2ElSFhAVQYxS6fwoxrFvr5xrM6xN-y0OH7OJ_OfNrzLN4Es6ww=w640-h369-no`
:status: published

@ **Ohio Linuxfest**, *Virtual*

..
  Google Photos Album: https://photos.app.goo.gl/LUXeip6Xz85QRTn78

`Slides <https://docs.google.com/presentation/d/1BnCyFaq_yDQMpGsGNcsVLQeVmer9JnVh4CuCS1wOK_c/edit?usp=sharing>`_
`Main Blog Article <{filename}/programming/baremetal-riscv-renode-1.rst>`_

.. code-block:: giturl

   git clone https://github.com/y2kbugger/baremetal-riscv-renode.git

.. raw:: html

    <div class="videoembed-container">
    <iframe class="videoembed-iframe" src="https://www.youtube.com/embed/JkeRezvCVfM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>

Explore the line between hardware and software by writing code with absolute control over the cpu and peripherals. We’ll explore how to do this using a completely free and open source simulator (Renode), toolchain (GCC), and instruction set (RISC-V). Using assembly, we’ll initialize parts of the system such as CPU interrupts and privilege levels, and setting up a call stack so we can use C. Using C we’ll build a handler for serial IO. Finally we’ll talk about the next steps in building a toy operating system such as building a simple monitor menu, memory management, and multitasking.

Bio:
Zak Kohler is a Chemical Engineer by education but true computer geek at heart. He started programming in 3rd grade and has never looked back. Often zak states that his biggest regret is not finding Python and Linux sooner...that didn't happen until university. Electronics is his second love and he fuses the two by playing with early computer hardware as well as modern microcontrollers. When zak isn't messing with computers he can be found turning milk into cheese, drawing, or exploring the world on long walks.
