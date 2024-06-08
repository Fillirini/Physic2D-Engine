from Math.Vector2 import Vector2
from Phys2D.Primitives.Shape import Shape


class Polygon(Shape):
    vertices: list[Vector2]

    def __init__(self, position: Vector2, vertices: list[Vector2]):
        super().__init__(position)
        self.vertices = vertices

    pass
