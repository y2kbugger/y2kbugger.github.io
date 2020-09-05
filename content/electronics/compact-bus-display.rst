A Compact 8-bit Bus Display
###########################

:date: 2017-12-19 20:58:08
:tags: retrocomputing, display, resistor-network, z80
:author: zak kohler
:summary: Prototyping front panel display components for a Z80 or TTL minicomputer.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cBalSP4v9ccpbxUJh9GvoOm17yEIM7RKbHRytZBRG3nFXhiVK3gzi0doJjcABb-UgmT6YEu4mHgpKo5I9wZqqnw8hDA0yYaoDn2vv8u4O4MlZbisDjxHfqNG20vVDOb1krMxj8qptTq9ZZoJmXSnGfWw=w605-h474-no`

..
  Google Photos Album: https://photos.app.goo.gl/XnXEAZp8C6Nqg5zJ3

Binary + Hex display module
===========================
What started out as a way to work on a prototype turned into a pretty cool display for a modular trainer.

Motivation
==========
I wanted an easy way to glance at the bus signals on my breadboard Z80 prototype. The goal of my Z80 computer is to learn about about what a cpu does, and watch it interact with memory and peripherals.

This means having features such as:

- writing to memory by hand
- stopping the clock
- single stepping the processor
- observe the state of the buses and I/O

This can be done either mostly in software, or mostly in hardware. When it's software we call it a monitor program, and for hardware it's commonly called a trainer. In my case, I want to add these features in hardware.

.. figure :: https://lh3.googleusercontent.com/pw/ACtC-3c0ghd2mox_6hFrde8tAXjk7DmhvGc71toNKh900qnj-BGMrMak8hZIL-LTVTdHAnEpbCeGC6tg72ETeG5O_yvcOw711jkv_MOECR1ghJIHX8-UBPcf0WgHlSIDumMk3i1R7e-_tDzwGP2CDNyK-RvCLw=w640-h273-no
   :width: 100%
   :alt: altaire
   :align: center

   The MITS Altair 8800. One of the first personal computers.

Flipping switches to bootstrap your paper tape driver `is very humbling <https://www.youtube.com/watch?v=5zbtNImG2NE>`_.

My trainer will be based on the Z80, having an 8-bit databus and a 16-bit memory address space. The first step was to get the cpu up and running and verify that the program counter was working. This can basically be done with resistors and power and a single LED. I got a lot of inspiration from `this video <https://www.youtube.com/watch?v=AZb4NLXx1aMchip>`_.


Input First
===========
First, I prototyped the "Keyboard" module.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fE2a-FpZLw8R6JkFSXoGRJ1Nfz_cHQOcbysIO11ySk9vkcqz00k0kcQITJES1ocRBrjHBSg4lDK5fZIIMVibu_l-NFW4GeA9fa_yBWb1nCgNYaKbCQ_Qp6TiIMvMiBsvjLeuT2U6j9kyVmKFVOBjoMpg=w960-h940-no
   :alt: the keyboard


Simple Prototype
================
Next, I wanted a simple way to test the keyboard module separate from the Z80. First I prototyped on a breadboard as shown above. The next step was to compact it into a module.

I wanted to make something compact that could be put into a breadboard to peek at the signals on a certain bus. I fell in love with the way the LEDs, resistor network, and header went together. This is functionally equivalent to the breadboard version shown in the "keyboard" photo.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dy7Eit3PbmaET6c6RsvxJtBAN3B4c14yo7qbImlrWUBt9yPcNIiw6sbGSteRL0b3DI9h51ugACrEwIm6x4eLPJNslq_RJj4ZWvpWGTe8rhIFcsnakEeJhLvKCTeq1RfZGN5K2UA81C0XTfE-k_5Vj3Gg=w405-h678-no
   :width: 70% 
   :alt: first 8 bit display prototype
   :align: center

But alas, this design had a problem.

I was getting some weird results when testing on the real Z80. I though I just needed to tweak the resistance to something less power-hungry. If you draw too much current, you might influence the levels you are trying to display. This would interfere with the operation of the Z80. I asked the datasheet: "is it possible to have a low enough current that I don't need to buffer when I am on the data bus for instance?" My CMOS Z80 can output one TTL load, so yes, but because it is active high but open collector you cannot source enough current in the "On" state. This is compounding by the fact the TTL levels are not actually 5 volts and therefore it might not actually have enough headroom to light some voltages of LED.

Buffers
=======
In order to overcome the issue of sourcing current, we can use a buffer. This repeats and optionally inverts a bus of signals. This solution probably seems obvious to someone who has worked with open collector buses before, but it took some research and deep reading of datasheets to understand what as going on here. It seemed overly complicated but is just the reality of open collect style buses. There are modern replacements for this such as tristate which pull in both directions but also have a high-impedance or 'Z' state. The Art of Electronics as a really good chapter on interfacing with peripherals and it covers this quite well.

This is the first prototype after realizing I really would need the buffer.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fCsSxakX4v-i5FCPm6vPRPEihtgqh8RpKpm1WuWQ5-h8Bp90ppqkQuCbi0IrAuOBX9LJmMCpq-YQP7Oen_cojJzra6_5WGsbq8lr4UIJz5oYpuVbG9QH3msjh4FqVyVTq4XJYbRdBX6GXYwJSPPjj3uQ=w521-h385-no
   :width: 100%
   :alt: 8 bit display
   :align: center

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3f5DpQtjzHHn8lq-yZM5X3mvM0KQHAO14yNFm6HxLgLdGr4tzcYancILEd0jg46RlqVD_Gquh9M3-vWcvUZLO7FdeF4_7z6loKC0K7Nv8KiYo3timjQH-OsBBlTBEnvK0QYJlYpxSW2jcpoTPBDEWTCNg=w960-h720-no
   :alt: module interface

Hex
===
Then I found some really cool hex displays on ebay. These have all of the decoding circuitry within them and so are easy to interface. I kinda became obsessed with this simplicity and so I found some rotary switched which have the hex encoding built into the mechanics of the switch. 

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dU-LMcUtXz-VFN-DtQIAu1TvNrymMRF7iTXfd_Lu285yQRt8Ia-CxIuPeXT5uCcOfsdNSyiImny9eodmNzx3366e8Fj5bKM6ZLFn-lvrPHXvod9bzuWCVOt8SKcXt8yCZUnuu2DWatDmheiabl6pf_Jg=w742-h989-no
   :width: 100%
   :alt: 8bit Dual Hex Display
   :align: center

These switches are used in "Keyboard 2.0".

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3d0Ws9WxGmbQcTa6gQo1WtSDn93HyQIFef4npbmYf6iQtYDPny-oCxkz81sOERbAXTqjwByfSZWgF4JzVUIbXkG3l8GLN_8myWvce-xSFMXxROrSkDHp2s28Emio5u1M974dw7_zoss7AwC9ZK2GkUriQ=w961-h670-no
   :width: 100%
   :alt: 8bit Dual Hex Switch
   :align: center

Finalizing the Hex Display
==========================
I came upon a kit for making 16bit ribbon cables that fit right onto header pins. I incorporated this into a tight layout but I wanted a clean way to do the point to point soldering.

After some research I found a good description of a method here: http://elm-chan.org/docs/wire/wiring_e.html. The suggestion to build a self tensioning pen is great and the quality of the result was impressive.


.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dgPGS6tIFvmjc0gPdEpUCdqg5weQKgYh5o3MoA_neKh27fXzBm3aP_ATOJqVHAGDN69Fe8zo-9bJxO-rXvuUu9fftDFphJhYZ0agR31vsqVUdr6gr4nxStLchkKfHXvPS46CnzKj8NWtdTxHx_plyl3g=w363-h323-no
   :alt: Example Wiring

I was inspired to replicate this technique.

Here's my toolkit:

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3exmk66BYn7wxr9Q9NwvLEuGKt4yzEWtqVquo6iev10d8Hf3UwvPej9Zap-QMEYEclulRcfgodmNR6B7OJ2IvZTdL0LSp9EstOVsPzknRKCCqWtIt0Q0O3kXXsv9jOmelLwlVg4tRBGD-ljDzqSqtzQ5w=w960-h723-no
   :width: 100%
   :alt: Home made toolkit

Tension kept by the viscus damping of a kneadable eraser.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3ePhwZ9b9fIGAGzAA_DDe35N_6GkRLwTrGekPlQyUMnyCYBujFzg-zPQkrmE_Ll6hzvmrMZmaPPBK0L94SeRMX_UT7P2ohYhYi3INMbyPdT5aMiCi9lk3MIthv12Pbzm7cEl--dBQprZYnQKkZRnMtw4Q=w671-h989-no
   :alt: Tension kept by the viscos damping of a kneadable eraser.

Amazing how nice it is to route using this simple device.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3ezmfiN2uOTWuMyl3MHJzX6RxCn4G41zBZFEJe9LNkCR3SJb-fjD0Mx3JTCJ2pE-0nD6SaByJltRPGrJc_ZNtfMOOR9WT6ONl2HjGrsPmnIH3zT-xpeTQZYTdUq8L_LdJdn6bYt1gh7HsnQGqh0Bqi7rg=w752-h989-no
   :alt: front end of the wiring pen.

First layout

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fqebsm0GTx7DqcircrdSlbVc5iyjbnIW3YTWwTKk3lCJ6AjnPWBSsws5IZSn37T9HsL__UqSfRB9oZ3uS9cL4GE9M_bmOd19GwdK3qwRGjX1bcGsvOvS4mV0pdO3c3B3N80lT-sFYV5zS-US1pKrsytg=w787-h989-no
   :alt: Original Layout.

Hold the pieces in place with gaffers tape

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fXwmP759cJQh0MwywwbvuxqR2uZl5Y1IkEZBU-FXB-QuBgzgQg3VVT3k24ibbBctvESS_WDwbW2iP5wc6sjAnkcMa1uXVy00cw1Ulza3YZo3U1Tatj2B0A5LGqHJgMLXEwo8EwpsN4u9JO7lm2iBY5yA=w742-h989-no
   :alt: holding pieces with gaf tape

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3efzzHBPWMn256AYGDUWSWhWS0ZYvOlyQ0KWivKxk7cvamg7CBJDLHTVfMd6ASrW2ew-Gkky5aQRufsOJiGiRxgPcsnItF51LuW95ftM3qgUq0IbFDAJSoF5kSJuRxAQPwWin_tpZesOul9nyvg2z_j6g=s960-no
   :alt: Fine wiring

It's alright to have crossing wires because we only remove enamel at the solder joint.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dXtlvsc8phKZQBTGvsIZoRiU25C0tyOfv3nC4Mg0fyfl94NLjZ39e_keXr6QC8AlLCuDtA-nOlJy0J0wFomY4-3QwpOYGpuebMZlzxSF5BpLSX3UdYd99hwPhsSZDdPo-LGz7dxFyVkqpFUq3_wyNIJQ=w570-h989-no
   :alt: Backside, crossing wires

These two devices are equivalent, each having a 8 bits of hex and 8 bits of binary. The final module is satisfyingly compact.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3dNRdys80vZDo2Yjc06wpy94Xq_PGtWSMmVyGzDddIox1RXK7uT77T6Qt2JKLiGai-1ERXvmmGCHEtdszBy4o-rw7gcMQbiSZFGS6iZIJcn2wDPkqvSFyxC0QwO1UJ_q4-tshn3hiKMIPuqbV_6T5koyw=w960-h775-no
    :alt: Size comparison

Driving the finished module with an ardunio to test.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eclInsbfzOgu6H4e9nNESdtCFPdL3JA8iWfcpG9dvcJC5xj554EXis4rYAPzbyzwEWUKt2jIbGPfvSvXZXH75SE8wOwV9YGUYm54DPQBwuf_cZl-7UE4JmJSdQEOK7iy8CKXLjYMo-hvA2m8IOohrK4Q=w617-h940-no
   :alt: it works
