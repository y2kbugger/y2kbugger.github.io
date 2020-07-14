Shower Speaker
##############

:date: 2020-01-23 00:00:00
:http://localhost:8000/index.htmlmodified: 2020-07-13 21:15:19
:tags: audio, cheap-modules
:author: zak kohler
:summary: How I turned a light fixture into a bluetooth speaker.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3fdCEYn2h_BHErDl3GDAmAzHG9qub7arCd6DKxiEwZvcMo2UjfukPEUGQXhrPeuijRr_mg8QM5W63TqsP1ZokHe7lj6M1JesicdmZpHOOfWkmpNfnEfkKgavAirG2Pp58GR0rrgkCoqnTSVaG3sQyiwow=w683-h550-no`

..
  Google Photos Album: https://photos.app.goo.gl/PUs3gPhkiMCq87nNA


Chasing the dream, shower + music
=================================
I have have numerous methods for listening to music and talks in the shower. The first one was a waterproof, battery powered AM/FM radio. The reception was crap. Over the years, other solutions included bluetooth speakers of various quality.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3e-UXvlfryZbjFfKdu8C9Scfgb_MKWgleQf4XdiA1egEa65oW__iavHXBEk026fI3erJyopEHpfkRPK1fhdW3Rz6RTaogGme3ZuZpQGs4nt1rTS-BL2VIYbZBS9ulICZddxjBBZ7UB6fkGMylSXYULxJA=w683-h554-no

The problem is that it is quite hard to get a speaker loud enough from outside of the shower. Before I moved I had pretty good results with a google home mini and double-sided tape. The new house though has sliding glass doors and that wouldn't work.

For a while I had given up and just brought my phone in.

Take it up a notch
==================
In the new house, I started thinking about modding the light fixure for sound.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3e6znAbqLyEvB-bbI5jW2m10e68eZp7LuUQdQRYXmcMKSTKb_ev4HwbWqyOBNrttaRZx6xqcPWw_AjuYkEoerHotvrIN2ymGjQ0UXTeE6DROp9iNDyE-SypDFEe5aXYesS2qprYJRmKaesGlKOWsN7P3Q=w683-h303-no
   :width: 100%
   :alt: light fixture in place.

After some thinking, I thought I had my options:

- Google Home Mini inside the light.
- Round speaker to replace the light.
- Keep using phone.

But while I was looking for a suitable speaker I remembered something I had seen on youtube.

https://www.youtube.com/watch?v=CKIye4RZ-5k

It is basically a voice-coil that can be attached to a flat surface to turn it into an active acoustic radiator. That's fancy for "speaker".

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eG2MHqqrY9s8Fvr3d8dyjg3PWyTTtZj3jTuWcoD56R9TXiW0WYvyMZKN1EqII8JDodt_eV4ob_mmwqSxjyMKUBTs_Tm4YRTm9j1WpQQ5HEr9xCeWDvR8Dmj14Cdc_isX23sSqrs2lDbLvdMbDyNouDAw=w683-h379-no
   :width: 100%
   :alt: Voice Coil Exciter

I figured this would be great because it would maximize the surface area of the speaker, and it would also allow me to continue using the light fixture normally. It could also be reversibly installed.

Parts List
==========
Goal: Integrate using cheapest junk modules available from internet.

- Voice coil - `$16.89 <https://www.amazon.com/gp/product/B00CWEJJ9K>`_
- Bluetooth Module - `$2.89/ea <https://www.amazon.com/gp/product/B07W4PJ469>`_
- Amplifier - `$5.99 <https://www.amazon.com/gp/product/B01HXU1G02>`_
- Power Supply - Had on hand

Interesting bits
================

Mixing signals
--------------
Since almost all bluetooth receivers are stereo I had to mix the signals. 

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fzgcIRnJm_WSAoTRZiZII9eRo6IixOsC9C7dHf8LBkvV9I0XxBWdkoA4gXzaJb2-Wg9cDVItT6miSOQRvwjTGlWyRVSGkg5jIv6j6Y4tXcSesvlGZU-bi62LuYc7__TzKHO7iLx0KbAfeR_QEjUwLPdQ=w683-h210-no

Delay on for amplifier
----------------------
I needed to design a delay circuit for the amplifier for two reasons.

Annoying connection chimes
^^^^^^^^^^^^^^^^^^^^^^^^^^
The default recording for "connected, on, etc" are annoying in general. The fact we have this tied into the light means it would have made annoying noises throughout the day, and worse, at night.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3f0f0xTF-5QaNQTsobny7fP42nz5yWxh4n8PD0Et2glHwegVbOD_mDwXXmkXL2VdbbXON_LRYF-ku1esiC9Fq_XKNvjNJvQCwEMEDnSJQ1ff3zlDJPJTPfIm3USgICtrEAEUo0xwGRzcsN_IGEFZXV5sw=w509-h678-no
   :width: 50%
   :alt: Relay for the delay circuit

   The relay controls the power amplifier as part of the delay cirbuit.

Turn-on thump
^^^^^^^^^^^^^
Secondly, if the amp turned on before the bluetooth, very loud "turn-on" thumps came through. I am proud of the hack for this one: I used an RC circuit to couple the delay to the status LED. The duty cycle of the "Connecting" blink would delay the amplifier indefinitely; however the solid "Connected" glow would put the amplifier on just after the crappy "connected" alert sound played.

.. figure:: https://lh3.googleusercontent.com/pw/ACtC-3dnWCOy3eCENtzF1VHMip7d2U9Qkxtl8Pa04Cuam66RBw0o0ihfcXctOZn57SLWRKRq95t_4_iVA2HZdr34dkigg1R47nnP9vmtzRfF3o-0FqZc_pFsE3RjYLWjUzpwUvv7OVwuqq2u-bOZneFfUt5b2Q=w683-h513-no
   :width: 100%
   :alt: Tuning by trial and error.

   Tuning the delay circuit to have an indefinite hold in the "Connecting" state.

Bad documentation
-----------------
Documentation for the bluetooth module was wrong and the "multi-purpose" button needed to be tied to ground to prevent phantom triggering. In hindsight this was obvious, but it was trust myself and disregard their schematic. Intermittent connection failures plagued me during almost the entire project. It was just infrequent enough to allow me to work through all the other parts of the project, but not enough to pinpoint the problem quickly.


Final State
===========
I installed everything in a way that I could reverse everything easily in case we leave. The sound is incredibly loud, and the quality is decent. As the shower is all smooth surfaces, it can be a bit echoey. Maybe some foam/fiberglass would help, but I don't want this thing catching fire. Overall I'm extremely happy with how it turned out.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fvLHQzYoWrGIsLTRfDj1ojHNkg8LIswD4eIPcDIDBS2xY3KXA7di_qyv5YifKOyI9_xw1qzfRrJWfyhIKF7hmJdqKBd1mRuPmX9828OSZjqoPsac2v36P0wqug6CQuGyh3sdf7nND3sklTSGL50cMsfQ=w683-h513-no

And of course it still works as a light.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3fvLHQzYoWrGIsLTRfDj1ojHNkg8LIswD4eIPcDIDBS2xY3KXA7di_qyv5YifKOyI9_xw1qzfRrJWfyhIKF7hmJdqKBd1mRuPmX9828OSZjqoPsac2v36P0wqug6CQuGyh3sdf7nND3sklTSGL50cMsfQ=w683-h513-no
