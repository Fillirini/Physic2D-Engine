from Math.Vector2 import Vector2
from Phys2D.Primitives.Shape import Shape


class Circle(Shape):
    radius: float

    def __init__(self, position: Vector2, radius: float):
        super().__init__(position)
        self.radius = radius
    pass
