from Math.Vector2 import Vector2
from Phys2D.Primitives.Shape import Shape


class Polygon(Shape):
    vertices: list[Vector2]

    def __init__(self, position: Vector2, vertices: list[Vector2]):
        super().__init__(position)
        self.vertices = vertices

    #test
    def rotate(self, degree):
        theta = math.radians(degree)

        cos = math.cos(theta)
        sin = math.sin(theta)

        for vert in self.vertices:
            distance = vert - self.position
            vert.x = self.position.x + distance.x * cos - distance.y * sin
            vert.y = self.position.y + distance.x * sin + distance.y * cos
        pass

    pass
