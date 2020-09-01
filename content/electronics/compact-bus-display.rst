A Compact LED 8-bit Bus Indicator
#################################

:date: 2017-12-19 20:58:08
:tags: retrocomputing, display, resistor-network, z80
:author: zak kohler
:summary: Prototyping front panel display components for a z80 or TTL minicomputer.
:status: draft

..
  Google Photos Album: https://photos.app.goo.gl/XnXEAZp8C6Nqg5zJ3

Blinkenlights, Binary and Hex
=============================

I walk through my experimentation that lead to a satisfying design for my front panel bus visualizer.

Motivation
==========
The goal was to make an easy way to glance at the bus signals on my breadboard Z80 computer. The purpose of this project is to learn about what the cpu is doing, and watch it happen.

This means features such as:

- writing memory by hand
- stopping the clock
- single stepping the processor
- observe bus-transfers and IO

This can be done either mostly in software, or mostly in hardware. When it's software we call it a monitor program, and for hardware it's commonly called a trainer. In my case, I want to add these features in hardware..

.. figure :: https://lh3.googleusercontent.com/pw/ACtC-3c0ghd2mox_6hFrde8tAXjk7DmhvGc71toNKh900qnj-BGMrMak8hZIL-LTVTdHAnEpbCeGC6tg72ETeG5O_yvcOw711jkv_MOECR1ghJIHX8-UBPcf0WgHlSIDumMk3i1R7e-_tDzwGP2CDNyK-RvCLw=w640-h273-no
   :width: 100%
   :alt: altaire
   :align: center

   The MITS Altair 8800. One of the first personal computers.

When you have to flip switches to input your bootstrap and paper tape driver by hand `it is very humbling <https://www.youtube.com/watch?v=5zbtNImG2NE>`_.


Simple Prototype
================
My trainer will be based on the Z80, having an 8-bit databus and a 16-bit memory address space. The first step was to get the cpu up and running and verify that the program counter was working. This can basically be done with resistors and power and a single LED. I got a lot of inspiration from `this video <https://www.youtube.com/watch?v=AZb4NLXx1aMchip>`_.

Next, I wanted a simple way to see that things were happening on the data and address
bus.

First attempt was just hooking up simply hooking up LEDs directly. I wanted to make something compact that could be put into a breadboard to peek at the signals on a certain bus. I fell in love with the way the LEDs, resistor network, and header went together.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dy7Eit3PbmaET6c6RsvxJtBAN3B4c14yo7qbImlrWUBt9yPcNIiw6sbGSteRL0b3DI9h51ugACrEwIm6x4eLPJNslq_RJj4ZWvpWGTe8rhIFcsnakEeJhLvKCTeq1RfZGN5K2UA81C0XTfE-k_5Vj3Gg=w405-h678-no
   :width: 70% 
   :alt: first 8 bit display prototype
   :align: center

But alas, this design had a problem.

I was getting some weird results so I though I just needed to tweak the resistance. If you draw too much current, you might influence the levels you are trying to display. This would interfere with the operation of the Z80. Is it possible to have a low enough current that I don't need to buffer when I am on the data bus for instance? My CMOS Z80 can output one TTL load, so yes, but because it is active high but open collector you cannot source enough current in the "On" state.

Buffers
=======
In order to overcome the issue of sourcing current, we can use a buffer. This repeats and optionally inverts a bus of signals. This is obvious to anyone to anyone who isn't a noob, but you gotta learn at some point.

Here is the first prototype after realizing I really would need the buffer.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fCsSxakX4v-i5FCPm6vPRPEihtgqh8RpKpm1WuWQ5-h8Bp90ppqkQuCbi0IrAuOBX9LJmMCpq-YQP7Oen_cojJzra6_5WGsbq8lr4UIJz5oYpuVbG9QH3msjh4FqVyVTq4XJYbRdBX6GXYwJSPPjj3uQ=w521-h385-no
   :width: 100%
   :alt: 8 bit display
   :align: center

Then I incorporated this along with a hexadecimal display.
