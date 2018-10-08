A Compact LED 8-bit Bus Indicator
#################################

:date: 2017-12-19 20:58:08
:tags: retrocomputing, display, resistor-network, z80
:slug: compact-bus-display
:author: zak kohler
:summary: XXXXXXXXXXXXXXXXXXXXXXXXXX
:status: draft

Blinkenlights in Binary and Hex
-------------------------------

I will walk through my experimentation that lead to my final design for my front panel bus visualizer.

Motivation
----------

This is made as a component of my single board Z80 trainer. Defining my Single
Board Computer (SBC) as a trainer basically means that its purpose it expose as
much implementation as possible to the user. This means entering machine code
by hand into memory, stopping the clock and directly examining memory. This can
be done either mostly in software, or mostly in hardware. If you really want to
bootstrap yourself from bare metal then it helps to build some of this monitor
functionality into the hardware.

.. image:: https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Altair_8800_at_the_Computer_History_Museum%2C_cropped.jpg/640px-Altair_8800_at_the_Computer_History_Museum%2C_cropped.jpg
   :width: 99%
   :alt: altair
   :align: center

When you have to type your bootstrap and paper tape driver by hand, `it can be a magical experience <https://www.youtube.com/watch?v=5zbtNImG2NE>`_.


Simple Beginnings
-----------------
My SBC trainer will be based on the z80, having an 8-bit databus and a 16-bit memory address space. First step was to get the
up and running and verify that the program counter was working. This can basically be done with resistors and power and a single LED. I got a lot of inspiration from `this video <https://www.youtube.com/watch?v=AZb4NLXx1aMchip>`_.

I wanted a simple way to see that things were happening on the data and address
bus.

Needed to decided on the resistance to use.
Don't want to interfere with the operation of the Z80. Is it possible to have a
low enough current that I don't need to buffer when I am on the data bus for
instance? My CMOS Z80 can output one TTL load. ** elaborate. Because it is active high but open collector you cannot source enough current in the "On" state.
Because of the resistor network multiple leds could get lit.


First attempt was just hooking up straight LEDs.

Then tried to make a simple tiny bus.

Here is the first prototype after realizing I really would need the buffer. 

.. image:: https://lh3.googleusercontent.com/ZTkNGM90GbQT8HR81Rduccpxjj79qDLCY-85zkK3d7mkg_VRtMOqrp16hxp4TQbGaku3aU63lVxi4A0cvnjfDfOIo65njsBgHUzoM53d2TlL5aKNgpNWbP8hNK2NK3HrGteIINT4AZYWX7icQdwNDAy7vMvNwKddkttm30-fwabXxzjacTN9rJ8zyG9ppb2XhPEkxyD_K4zs7H8MXh05IJgKW1QZo40tZtwoZFfuRPJv1JKYs1iHFEZuV476mOVL3GjvPr_iCFiV7nwQVKxnaYDugkJbgfoRQKBHmKlyozC1lU_vbIPMJ8TDyyFe7fpQk5ZE6CSben5H9Br98RtM_9bSuSlCS8guK1oJbbVvx_Q6n_BHFBznelrsgHVUdH0zT08Y23mG8Oqo_TEzpa2g50kRNR5b0_eeZAsiwFGc5o2z4PAw5ETGI8ZUdabBP2G6kjECVhMfEkjgQVK13Sh0kLk4qfcbu9zcJttApBr8AdavU7bs1vF008qQbsR5BQIk_P1QLpl1cCtA8IcBOlDBiQ53Beq19Cdd-zZXFJsXwlTKH0KMRip4CtiBkyir29qylmWZ61WSR3NQdkGPCRbllEPBKwIGGnuEnJdGcyZMbx-B5Hukcko6urYcFKn_olunzLcKveFFHo5SlkDkAW9fWHRXWVwBUs31mP-DQWjoiw7mZDpp5FVMU9G3Yw=w521-h385-no
   :width: 100%
   :alt: 8 bit display
   :align: center

Then I incorporated this along with a hexadecimal display.
