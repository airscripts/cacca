from typing import Any, Generic, List, NewType, NotRequired, TypedDict, final

from cacca.types.generics import Action, Guard, Hook, T


@final
class Sublayer(TypedDict, Generic[T]):
    action: Action[T]
    hook: NotRequired[Hook[T]]
    guard: NotRequired[Guard[T]]


@final
class Subcargo(TypedDict, Generic[T]):
    hook: NotRequired[T]
    guard: NotRequired[T]
    action: NotRequired[T]


Cargo = NewType("Cargo", Subcargo[Any])
Layer = NewType("Layer", Sublayer[Any])
Layers = NewType("Layers", List[Layer])
