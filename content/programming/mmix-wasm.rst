MMIX, WASM, What?
#################

:date: 2018-03-04
:modified: 2020-05-18 13:14:09
:tags: assembly, algorithms, MMIX, TAOCP, books
:author: zak kohler
:summary: Compiling the MMIX Assembler and Simulator to Web Assembly
:status: draft
:cover: `https://lh3.googleusercontent.com/pw/ACtC-3cmwaXo3THz54nq3bz9bWJ9N3hK5zfHL9o4JAsdri5mZ7AgP4LPpilaSkxatNxccRDbxKgZ65jDB08Akq1UMV1nGGqktUrq8uXJFhs9ODgtUQ1wT6SAapWlK5zTWLP-tliFKDBuARvEVYmHnRilf89CsQ=w572-h85-no`

..
  Google Photos Album: https://photos.app.goo.gl/dfXck6rcLDcZHtv17

Fast feedback for The Art of Computer Programming Exercises
===========================================================
As a started working through the `exercises in TAOCP <https://blog.y2kbugger.com/reading-taocp-mmix.html>`_, I wanted a quicker way to work on the problems in assembly language. I was also in the process of learning C so I was interesting in taking a peek at the
Link to first blog.


Explain why I wanted some rapid interation on simple assembly programs.

link to my repo and demo.

Give a string processing version of program.

Give high level of process.

Explain problems, Literate Programming Tools WEB etc, Issue with make files. and vestigial extension to MMIX.

Show shirt


Quick start section
===================
Here is the official quick start guide::
https://docs.getpelican.com/en/stable/quickstart.html

This guide is how to start from scratch. The guide below is about starting up the developer environment for writing the blog.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

My quick start subsection
-------------------------
Write subsubsection (use sparingly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Start up dev environment:

.. code-block:: bash

    $ wo-blog

- Add/modify the files in blog/content/CATEGORY/SLUG-OF-THE-PAGE.rst
- Saving the file will cause it to auto-update in the dev env browser window. This is done with javascript and only activated when local.

If you are satisfied with the post, set ``:status: published``, otherwise you can publish it to the web as a draft.

Tips:
    - Manually start the dev server in another xterm to see debug info
      ``$ pipenv run make stopserver && pipenv run make devserve``

Publish
^^^^^^^
Publishing makes the blog entry available to the world.

To publish, commit articles additions/changes:

.. code-block:: bash

    $ git add content/
    $ git commit
    $ git push origin write

Finally publish your changes:

.. code-block:: bash

    $ pipenv run make github

Style guide
===========
Article titles should be ``Title Case``, all other sections should be ``Sentence case like this``.

There should be no gap between a section header and the first paragraph.

Favor figures over images.

When in doubt, reference this article. For example, which style of links to use.

Metadata
========
Url comes from the file basename if you don't override it with slug::

    :slug this-is-alternate-url

The folder will be used as the category

Other Default info types::

    :date: 2018-01-25 19:54:15
    :modified: 2017-12-16 19:54:15
    :tags: bread
    :category: food
    :author: zak kohler
    :summary: Just testing some more formatting
    :status: draft

The default status is set to draft, to publish set it to published::

    :status: published

Content
=======
Content types that I commonly use within articles I'll put here. Otherwise here are the thorough guides.

- More about writing here https://docs.getpelican.com/en/stable/content.html
- https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- https://docutils.sourceforge.io/docs/user/rst/quickref.html#definition-lists

Linking
-------
Internal
^^^^^^^^
You don't have to make tags to link internally, you can do it just like this: `a link to an internal file <{filename}/food/no-knead-bread-one.rst>`_
I haven't figured out yet if there is a way to link to sub-sections

External
^^^^^^^^
Here is an inline link to an external site `Jungle Jim's <https://junglejims.com/>`_.

If you actually just want to show the external link, just put in it strait up like in the following sentence. Hey try http://google.com its good.

Inserting photos
----------------
All photos are hosted using google photos.

Here is an exact step-by-step for getting a correct hyperlink.

1. Make sure the album is shared via make link
   Here is the link for the Blog Misc. https://photos.app.goo.gl/dfXck6rcLDcZHtv17
2. Open the share link in incognito mode
3. Go to a specific photo in the album
4. Click on it to get a closer view of the image
5. Right Click on the Image
6. Click on “Copy Image Address”

When you add a bunch of pictures from a new album, be sure to add that album url in a comment.

..
    Comments are like this. https://photos.app.goo.gl/qfXck6rcLDcZHtv1d

Here is one of my good friends:

.. image:: https://lh3.googleusercontent.com/0pckhDWOKZKJEeB2izt77k40PlTPE0AYu8N4e-_RCaxgxUrUoZPQvGllBkYEbNYLfRg7GUQfxCC-le3jQYmTgUbJ4_ns59Ru-_8aaoiScEBAJdL2U5GutLXkM81mUvmik2u2RE1j6nQ=w460-h678-no
   :width: 100%
   :alt: Boojie
   :align: center

I hope to see you soon Booj

Figures are like images but include caption/subcontent.

.. figure:: https://lh3.googleusercontent.com/TQ_e5Ds-zAANFEZ8jwQDspm634t8TTd9mhgffJDgTClAv-m3-yDU7BEDelYqRZe4gAk-p21Dmsx9S0euK4m3ExzyZmmaTv7rKrEjS4UzwORAiFNy8WOg8vwC4xS19R_CX4dUkcUOs5g=w683-h419-no
   :width: 300px
   :alt: Good look at what stock prices happen.

   Here is where the caption happens. Anthing else can go here also. What else

Inline style
------------
*Italics use asterisk*

**bold is double asterisks**


``inline literal``

.. note::
   Do not confuse `interpreted text` with ``inline literal``.
   Interpreted text gets rendered as <cite>

Git clone to a tag
------------------
.. code-block:: giturl

   git clone --branch 2019-07-28-PyOhio https://y2kbugger@bitbucket.org/y2kbugger/sapy.git

Linking slides and jupyter notebook

`Slides <https://drive.google.com/open?id=1u8qlAK4SeqFX3ybT7zVuKWItMvCadhsgF9WmCCOM3dQ>`_ `Live Jupyter Notebook <https://gke.mybinder.org/v2/git/https%3A%2F%2Fy2kbugger%40bitbucket.org%2Fy2kbugger%2Fsapy.git/de5086ea943c94fec40e14478257ab2716e28c96?filepath=Simple%20As%20Possible.ipynb>`_

Definition lists
================
What
  Definition lists associate a term with
  a definition.

How
  The term is a one-line phrase, and the
  definition is one or more paragraphs or
  body elements, indented relative to the
  term. Blank lines are not allowed
  between term and definition.

Block quotes are just
=====================
    Indented paragraphs,

        and they may nest.

Recipe Ingredients
==================
For ingredients combine highlights directive with bulletless(pipe) lists

Wet
---
.. Highlights::
    | 1/2 c. unsalted butter
    | 2.25 c. sugar [#sugar]_
    | 6 very soft persimmons
    | 1.5 c. whole milk
    | 5 large eggs
    | 2 teaspoons pure vanilla extract
    | 1 lemon

-------

.. [#sugar] Is sugar wet today?


Code blocks
===========
A block followed by two colons will be monospaced::

    :date: 2018-01-25 19:54:15
    :modified: 2017-12-16 19:54:15
    :tags: bread
    :category: food
    :author: zak kohler
    :summary: Just testing some more formatting
    :status: draft


You can specify a particular language:

.. code-block:: bash

    $ cd ~/devel/blog
    $ pipenv run python

Here is a more detailed code block including line numbers:

.. code-block:: python
   :linenos:

    from htooze import world

    def test_planet_exists():
        p = world.Planet()
        assert isinstance(p, world.Planet)

    def test_life_can_exist():
        mycell = world.Cell()
        assert isinstance(mycell, world.Cell)

    def test_planet_starts_without_life():
        p = world.Planet()
        assert len(p.life) == 0

    def test_life_can_live_on_planet():
        p = world.Planet()
        mycell = world.Cell()
        p.addcell(mycell)

        assert len(p.life) == 1
        for coords, cell in p.life.items():
            assert cell is mycell
            assert isinstance(coords, tuple)
            assert int(coords[0]) == coords[0]


My architecture details
=======================

Git branches
------------
master
    This is the one with the compiled content, this syncs to the remote. No manual commit.
write
    This is the one that we develop in, make your commits here.

wo-blog
-------
- Open the project directory
- Checkout the write branch
- Kill existing servers and start a new one with all output piped to /dev/null
- Open up a chrome window to view new posts

Hosting
-------
Hosted as a gitlab page. Domain is setup with 1and1.

Had to edit dns setting inside of 1and1 per github guidelines.
