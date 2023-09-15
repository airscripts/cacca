from typing import Any, Generic, List, NewType, NotRequired, Optional, TypedDict, final

from cacca.types import Action, Guard, Hook, T


@final
class Sublayer(TypedDict, Generic[T]):
    action: Action[Optional[T]]
    hook: NotRequired[Hook[Optional[T]]]
    guard: NotRequired[Guard[Optional[T]]]


@final
class Subcargo(TypedDict, Generic[T]):
    hook: NotRequired[Optional[T]]
    guard: NotRequired[Optional[T]]
    action: NotRequired[Optional[T]]


Cargo = NewType("Cargo", Subcargo[Any])
Layer = NewType("Layer", Sublayer[Any])
Layers = NewType("Layers", List[Layer])
