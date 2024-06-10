from Phys2D.Primitives import *


def collision_detection_between_circle_and_polygon(circle: Circle, poly: Polygon) -> bool:
    for vert in poly.vertices:
        if Vector2.distance(circle.position, vert) <= circle.radius:
            return True

    return False
