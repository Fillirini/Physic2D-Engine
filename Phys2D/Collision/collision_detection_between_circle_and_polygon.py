from Phys2D.Primitives import *


def collision_detection_between_circle_and_polygon(circle: Circle, poly: Polygon) -> bool:
    for vert in poly.vertices:
        if (circle.position - vert).get_length() <= circle.radius:
            return True

    return False
