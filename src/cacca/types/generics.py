from typing import Any, Callable, Optional, TypeVar

T = TypeVar("T")

Args = Optional[Any]
KwArgs = Optional[Any]
GenericFn = Callable[..., T]

Hook = Callable[..., Optional[T]]
Guard = Callable[..., Optional[T]]
Action = Callable[..., Optional[T]]
