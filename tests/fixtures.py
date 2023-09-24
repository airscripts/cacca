# pylint: disable=redefined-outer-name
from pytest import fixture

from cacca import Cacca
from cacca.constants import ACTION_KEY


@fixture
def cacca() -> Cacca:
    return Cacca()


@fixture
def seed() -> Cacca:
    container = Cacca()
    container.insert({ACTION_KEY: print})
    return container


@fixture
def stashed(seed: Cacca) -> Cacca:
    seed.stash()
    return seed
