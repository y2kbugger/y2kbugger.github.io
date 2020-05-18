I am now a maintainer on the Arch User Repository
#################################################

:date: 2020-04-14 00:06:28
:tags: Linux, packaging, OpenSource, ArchLinux
:author: zak kohler
:summary: Just made my first submission to the arch user repository (AUR)
:status: published
:cover: `https://lh3.googleusercontent.com/5Dp87kkeAqmgWWjdXg54hgEvnva7Lf_WbI8pasROx0_uXiW_rshrOYIYofmeAwa8ufIyRhfxgiU1CbjWCDsTz9RSwaWn18-2Op3NjdzNfqQ1XkUbV6Fd5YfCz5X0TGJKK1IRDV6_lac=w503-h216-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

Long time user, first time maintainer
=====================================
I've been a Linux user for a decade now, Ubuntu at first, but I switched to `ArchLinux <https://archlinux.org>`_ after a year or two. I quickly found the `Arch User Repository <https://aur.archlinux.org/>`_ or AUR to be a treasure trove of free (libre) software; I am still in awe today. On ms windows, finding software meant downloading binaries from sketchy freeware sites. The prospects were better on Ubuntu since many software projects engaged with the community and produces regular releases. One drawback however were the stale repos, some packages on ubuntu were still pointing at releases that were years old.The Ubuntu `Personal Package Archives <https://launchpad.net/ubuntu/+ppas>`_ PPAs was supposed to solve this, but I never had  good luck with them. The packages always seemed random whether or not they were compatible and maintained.

.. image:: https://lh3.googleusercontent.com/mapAQeHjDZmDn4Jq-FXyEhuFDEB6IHuEBzk8egTflCpiwLU9g0-W_YevSXbZEE-tQopVtEIJLO_rkjgf2TjA_olTqV7gGPiiDPKliO23xXNlOENJnDhobYLeLh7w942lCrhiASjMVHA=w683-h228-no
   :alt: ArchLinux Logo

Enter ArchLinux, everything is on the bleeding edge. The vast majority of typical software needs is packaged and up-to-date. For more custom software, there is the AUR. It started as just people sharing recipes for building packages...and well, that's still the case and it's a *really* good thing too, it's beauty is in the simplicity. Packaging makes sure that the software you install goes in cleanly and can be removed without leftover files. You can think of ArchLinux as basically a package manger [#pacman]_ and a wonderful community. The AUR acts as a funnel for new packages to become official in the community repository, which are built packages rather than just recipes.

.. [#pacman] See pacman: https://wiki.archlinux.org/index.php/pacman

My contribution
===============
For my first contribution I wanted something simple, just to learn the process. At work I have been spending a lot of time with the conda package manager, and a few months ago I submitted my first conda-forge recipe. For a long time I have wanted to put something on AUR and now that packing is fresh on my mind I figure it's a good time to get this one under my belt. I chose a shell script that I have used for years; it is a fork of a now deleted AUR package. Since it's a shell script it still needs to be installed to the system but it doesn't have the complication of needing to be compiled.

.. image:: https://lh3.googleusercontent.com/Cc_WYvWQQrft1j2Qgb6mjuLL5t1zpBXlPVjViDqeBuPgJLK0Spus6pszYoEhzmO5gTY-NH2uJ44rq1CyeDapBKiJhOkhAKwJc77_sZpWv9JL9qgza5Yawd9ilg58bau2i1nR8vu6xEk=w503-h216-no
   :alt: My AUR package page

The package is called `dmenu-recent-aliases`, and it is a lightweight application launcher. It provides fuzzy searching for all the executables on your `PATH` and also includes your custom bash functions and aliases. I have added a few extra features as well, for the full docs see https://gitlab.com/y2kbugger-projects/scripts/dmenu-recent-aliases.

A second reason for choosing this one is that there is some demand for the script and the original is no longer being maintained.

.. figure:: https://lh3.googleusercontent.com/oh9j6EPpcdpLD-1pWDsRzv18wSoKxlbB_bMcunePT2W8DGunnHpAswL7riiCzTgzkyiQ_I0h_00VP-mDrfH3ZeHMmnCwn9PtHVUu219CopWoYB7GI-NQell_BQ3yM096_IMTp5bAXlk=w438-h78-no
   :alt: Broken link on aur

   The archwiki still has a link to the old package, but it no longer exists.

Become a maintainer yourself
============================
Before you start to make a package, you should be familiar how to manually install other's packages from the AUR. Avoid AUR helpers for a while, trust me.

Here is the quickstart guide:

https://wiki.archlinux.org/index.php/Arch_User_Repository#Installing_packages

As far as the packaging process goes, it's not too difficult but I can't begin to cover it all here. Instead, I recommend reading at least all of these:

- https://wiki.archlinux.org/index.php/Creating_packages
- https://wiki.archlinux.org/index.php/Arch_package_guidelines
- https://wiki.archlinux.org/index.php/AUR_submission_guidelines

It may also be helpful to check out my minimal `PKGBUILD` here.

.. code-block:: giturl

   git clone https://aur.archlinux.org/dmenu-recent-aliases-git.git

After you cobble together what you think is a good `PKGBUILD` you can ask for a review on the `#archlinux-aur` IRC. Try `IRCCloud <https://www.irccloud.com/>`_ if you aren't familiar with IRC.

Finally, submitting is as easy as a git push, but be sure all of your i's are dotted and t's are crossed.

Now you are <strike>all done</strike> just beginning. As a maintainer it's your job to keep the package up-to-date and incorporate suggestions from the community.
