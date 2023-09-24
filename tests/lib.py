# pylint: disable=redefined-outer-name
from cacca import Cacca, Cargo, Layer, Layers
from cacca.constants import ACTION_KEY, GUARD_KEY, HOOK_KEY
from tests.constants import EMPTY, PRINT_OUTPUT
from tests.fixtures import cacca  # pylint: disable=unused-import # type: ignore
from tests.fixtures import seed  # pylint: disable=unused-import # type: ignore
from tests.fixtures import stashed  # pylint: disable=unused-import # type: ignore

LAYER = Layer({ACTION_KEY: print})
LAYER_INPUT = Cargo({ACTION_KEY: PRINT_OUTPUT})
LAYER_OUTPUT = Cargo({ACTION_KEY: None, GUARD_KEY: EMPTY, HOOK_KEY: EMPTY})


class CaccaSuite:
    def tfngetters(self, cacca: Cacca) -> None:
        assert cacca.layers == []
        assert cacca.bucket == []

    def tfnsetters(self, cacca: Cacca) -> None:
        cacca.layers = Layers([LAYER])
        assert cacca.layers == [LAYER]

    def tfninsert(self, cacca: Cacca) -> None:
        layer: Layer = LAYER
        cacca.insert(layer)
        assert cacca.layers == [layer]

    def tfnremove(self, seed: Cacca) -> None:
        seed.remove()
        assert seed.layers == []

    def tfnstash(self, seed: Cacca) -> None:
        seed.stash()
        assert seed.layers == []
        assert seed.bucket == [LAYER]

    def tfnunstash(self, stashed: Cacca) -> None:
        stashed.unstash()
        assert stashed.layers == [LAYER]
        assert stashed.bucket == []

    def tfnrun(self, seed: Cacca) -> None:
        seed.insert(LAYER)
        res = seed.run(0, LAYER_INPUT)
        assert res == LAYER_OUTPUT
