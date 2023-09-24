from typing import Optional

from cacca.helpers import find, interact
from cacca.types import Cargo, Layer, Layers


class Cacca:
    __bucket: Layers
    __layers: Layers

    @property
    def bucket(self) -> Layers:
        return self.__bucket

    @property
    def layers(self) -> Layers:
        return self.__layers

    @layers.setter
    def layers(self, value: Layers) -> None:
        self.__layers = value

    def __init__(self) -> None:
        self.__bucket = Layers([])
        self.__layers = Layers([])

    def insert(self, value: Layer, index: Optional[int] = None) -> None:
        index = index or len(self.__layers)
        self.__layers.insert(index, value)

    def remove(self, index: int = -1) -> Layer:
        return self.__layers.pop(index)

    def stash(self) -> None:
        self.__bucket = self.__layers
        self.__layers = Layers([])

    def unstash(self) -> None:
        self.__layers = self.__bucket
        self.__bucket = Layers([])

    def clear(self) -> None:
        self.__bucket = Layers([])
        self.__layers = Layers([])

    def run(self, index: int, cargo: Cargo) -> Cargo:
        layer: Layer = find(layers=self.__layers, index=index)
        return interact(layer, cargo)
