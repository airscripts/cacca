from typing import Literal

from cacca.constants import EMPTY_LITERAL
from cacca.types import Args, KwArgs


def empty(*_: Args, **__: KwArgs) -> Literal["EMPTY"]:
    return EMPTY_LITERAL
