from Phys2D.Primitives.Circle import Circle


def collision_detection_between_circles(circle1: Circle, circle2: Circle) -> bool:
    distance: float = Vector2.distance(circle1.position, circle2.position)
    if distance <= circle1.radius + circle2.radius:
        return True
    else:
        return False
    pass
