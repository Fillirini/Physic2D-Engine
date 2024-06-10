from Phys2D.Primitives.Circle import Circle
from Math.Vector2 import Vector2


def is_point_in_circle(point: Vector2, circle: Circle) -> bool:
    distance = Vector2.distance(circle.position, point)
    return distance <= circle.radius
