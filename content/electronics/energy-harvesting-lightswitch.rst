Energy harvesting wireless switch?
##################################

:date: 2020-03-26
:modified: 2020-08-13 13:07:57
:tags: teardown
:author: zak kohler
:summary: Settling a bet of whether a wireless switch really didn't have a battery.
:status: published
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3e1pcK6VhYyIFg91zihsp8w7e9nSO3cSF1nDEVS4DLI0UFMD1PHxYkd0rWXgBNOSGo7R8NQIMLTfiMmC9PrqIpx9LVGSGF71q1Jt0iigbclF4qC-hIENJEj0azfWJJNvAXSAtw4vxTCNzfegz86OJ4pfA=w683-h513-no`

..
  Google Photos Album: https://photos.app.goo.gl/NwiirCi5DN8tfZqP8

Robust wireless light switch
============================
I was looking for a system of wireless switches that didn't rely on wifi. I wanted something standalone because of reliability and security. I noticed one brand advertised "no battery" and I took that at face value.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3e3prwqvj3a56qTJPbfABldmo3IkhC8qyUA-hQMQvfjgDAdBOoHMsoCTAzI85O0CJ7_4CWY1MkytaMcMZJrZ9Um_irie8TJzTkK5IOfanQZCBFIoD6gDQctsvO9ePqWhZYthBHM4cjlzgTPprOCVqv7XQ=w683-h264-no
   :width: 100%
   :alt: Amazon ad for acegoo switch
   :align: center

Too good to be true
===================
Sometime after installing I was talking to a co-worker and we started wondering: "Could it be a sealed lithium battery?" I knew this was done in the 10 year no maintenance smoke detectors, and I thought the "battery free" might actually be marketing lies.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eEjxUTaaF23O8dVz19PxDf7caH6lX0eH2OfvC3i9QWno-S8bUwrJWe22icYK_95z0cyQeo_E3ASTuOUXszwaWRlbKE6G8yyNIEQl4Lg7DPehRRJbfFhZ3mC29LrRFxwPuwhqRa6uAWOL4Jy5D-ADTNlA=w545-h678-no
   :width: 60%
   :alt: How the switch is used.
   :align: center

Teardown
========
A large mechanical switch, with a smaller module in the center. There are more membrane switches than one expect for an on off switch. The antenna was run around the outside.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3e1pcK6VhYyIFg91zihsp8w7e9nSO3cSF1nDEVS4DLI0UFMD1PHxYkd0rWXgBNOSGo7R8NQIMLTfiMmC9PrqIpx9LVGSGF71q1Jt0iigbclF4qC-hIENJEj0azfWJJNvAXSAtw4vxTCNzfegz86OJ4pfA=w683-h513-no
   :width: 100%
   :alt: Removing the case.
   :align: center

There are levers which are moved by the switch and seem to move something back and forth internally.

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3eam4ql5dpjHEB7kGDh28Vdq4zkvUHnVUczglv_y9HZpwTd5qKrNMH5at6RRGBqsBmi-g0KFc2hcFoKFY_rWDIKVgs6ofzoLT8gUS53uc0Q6QfeQNWk21qGmOPRCm15zUYCYCvu6UnhC_-sthopvhCpGw=w683-h329-no
   :width: 100%
   :alt: Levers
   :align: center

Aha, magnets and a coil, it really does generate its own power!

.. image:: https://lh3.googleusercontent.com/pw/ACtC-3cQPGUj_ta7hJ2nne7fHtr5S-rWLGC6o7--OqfTB7Umxolq0qH8iqd1wrLGGYLsYyJad4dTfShZOrgBVWvBhJJJ7eeqJjcgt4OZI-e8-d96kC8506VMQPcYerhZnFbLOMZ7GxOPyVgP114q5FITNwIXEQ=w532-h630-no
   :width: 100%
   :alt: Coil and magnets
   :align: center
