My Intial Commit
################

:date: 2017-12-15 23:12:30
:modified: 2017-12-15 23:12:30
:tags: testing
:category: not-real
:slug: initial-commit
:author: zak kohler
:summary: Verifying everything is set up correctly.

This is a draft that will never be published


subtitle
--------

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


more
real

