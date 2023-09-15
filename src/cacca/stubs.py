from typing import Literal

from cacca.types import Args, KwArgs


def empty(*_: Args, **__: KwArgs) -> Literal["EMPTY"]:
    return "EMPTY"
