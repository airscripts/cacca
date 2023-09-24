from typing import Literal

from cacca.types import Args, KwArgs

EMPTY_LITERAL = "EMPTY"


def empty(*_: Args, **__: KwArgs) -> Literal["EMPTY"]:
    return EMPTY_LITERAL
