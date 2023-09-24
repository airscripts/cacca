from typing import Dict, Literal

from cacca.stubs import empty
from cacca.types import Action, Guard, Hook

HOOK_KEY = "hook"
GUARD_KEY = "guard"
ACTION_KEY = "action"

EMPTY_HOOK: Dict[Literal["hook"], Hook[Literal["EMPTY"]]] = {HOOK_KEY: empty}
EMPTY_GUARD: Dict[Literal["guard"], Guard[Literal["EMPTY"]]] = {GUARD_KEY: empty}
EMPTY_ACTION: Dict[Literal["action"], Action[Literal["EMPTY"]]] = {ACTION_KEY: empty}
