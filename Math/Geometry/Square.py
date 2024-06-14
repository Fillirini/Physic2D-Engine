from typing import override

from Math.Geometry.Rectangle import Rectangle
from Math import Vector2


class Square(Rectangle):
    def __init__(self, pos: Vector2, length: float):
        super().__init__(pos, length, length)
        pass

    pass
