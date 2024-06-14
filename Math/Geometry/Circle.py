from Math import Vector2
from Math.Geometry import Shape


class Circle(Shape):
    radius: float

    def __init__(self, pos: Vector2, radius: float):
        super().__init__(pos)
        self.radius = radius
        pass

    pass
