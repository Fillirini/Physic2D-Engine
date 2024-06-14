from Math import Vector2
from Math.Geometry import Shape


class Polygon(Shape):
    vertices: list[Vector2]

    def __init__(self, pos: Vector2, vert: list[Vector2]):
        super().__init__(pos)
        self.vertices = vert.copy()

    def get_normals(self): pass

    pass
