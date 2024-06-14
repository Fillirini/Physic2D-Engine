from typing import override

from Math.Geometry import Polygon
from Math import Vector2


class Rectangle(Polygon):
    def __init__(self, pos: Vector2, width: float, height: float):
        bottom_left = Vector2(-width, -height)
        top_left = Vector2(-width, height)
        top_right = Vector2(width, height)
        bottom_right = Vector2(width, -height)

        super().__init__(pos, [bottom_left, top_left, top_right, bottom_right])
        pass

    @override
    def get_normals(self):
        edge1 = (self.vertices[0] - self.vertices[1]).normalize()
        edge2 = (self.vertices[1] - self.vertices[2]).normalize()

        normal1 = Vector2(edge1.y, - edge1.x)
        normal2 = Vector2(edge2.y, -edge2.x)
        return [normal1, normal2]

    pass
