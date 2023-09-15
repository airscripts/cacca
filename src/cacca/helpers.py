from typing import cast

from cacca.constants import ACTION_KEY, EMPTY_ACTION, GUARD_KEY, HOOK_KEY
from cacca.stubs import empty
from cacca.types import Cargo, Layer, Layers


def find(layers: Layers, index: int) -> Layer:
    try:
        return layers[index]

    except IndexError:
        return cast(Layer, EMPTY_ACTION)


def interact(layer: Layer, cargo: Cargo) -> Cargo:
    hook = layer.get(HOOK_KEY, empty)
    guard = layer.get(GUARD_KEY, empty)
    action = layer.get(ACTION_KEY, empty)

    res: Cargo = {ACTION_KEY: None, GUARD_KEY: None, HOOK_KEY: None}
    anchor = None

    anchor = guard(cargo.get(GUARD_KEY))
    res[GUARD_KEY] = anchor

    if not anchor:
        return res

    anchor = action(cargo.get(ACTION_KEY))
    res[ACTION_KEY] = anchor

    anchor = hook(cargo.get(HOOK_KEY))
    res[HOOK_KEY] = anchor

    return res
