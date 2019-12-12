A Second Article, wondering what this would look like if the title was longer
#############################################################################

:date: 2017-12-16 19:54:15
:modified: 2017-12-16 19:54:15 
:tags: testing, more testing, nothing-important, fake
:slug: second-has-longer-title
:category: fake
:author: zak kohler
:summary: Just testing some more formatting

First Heading in Article
-------------------------

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

I am only doing `testing <{tag}testing>`_ right now, real to come soon.

this is good code:

.. code-block:: bash

    $ pipenv run python

the end cool


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

Here is one of my good friends:

.. image:: {static}/images/758_bwneg11-024.jpg
   :width: 100%
   :alt: Boojie
   :align: center


I hope to see you soon Booj
