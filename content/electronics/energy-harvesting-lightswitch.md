---
title: Energy harvesting wireless switch?
date: 2020-03-26
modified: 2020-08-13 13:07:57
tags: teardown
author: zak kohler
summary: Settling a bet of whether a wireless switch really didn't have a battery.
status: published
cover: /img/2020-03-26__energy-harvesting-lightswitch__cover.jpg
---

## Robust wireless light switch
I was looking for a system of wireless switches that didn't rely on wifi. I wanted something standalone because of reliability and security. I noticed one brand advertised "no battery" and I took that at face value.

![Amazon ad for acegoo switch](../img/2020-03-26__energy-harvesting-lightswitch__acegoo-ad.png)

## Too good to be true
Sometime after installing I was talking to a co-worker and we started wondering: "Could it be a sealed lithium battery?" I knew this was done in the 10 year no maintenance smoke detectors, and I thought the "battery free" might actually be marketing lies.

![How the switch is used.](../img/2020-03-26__energy-harvesting-lightswitch__how-used.gif){: width=60% }

## Teardown
A large mechanical switch, with a smaller module in the center. There are more membrane switches than one would expect for an on off switch. The antenna was run around the outside.

![Removing the case.](../img/2020-03-26__energy-harvesting-lightswitch__removing-case.jpg)

There are levers which are moved by the switch and seem to move something back and forth internally.

![Levers](../img/2020-03-26__energy-harvesting-lightswitch__levers.jpg)

Aha, magnets and a coil, it really does generate its own power!

![Coil and magnets](../img/2020-03-26__energy-harvesting-lightswitch__coil-magnets.jpg)
