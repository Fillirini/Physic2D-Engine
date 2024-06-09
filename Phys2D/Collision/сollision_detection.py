from Phys2D import *
from Phys2D.CollisionDetection.collision_detection_between_circles import collision_detection_between_circles
from Phys2D.CollisionDetection.collision_detection_between_polygons import collision_detection_between_polygons
from Phys2D.CollisionDetection.collision_detection_between_circle_and_polygon import collision_detection_between_circle_and_polygon


def check_collision(body1, body2) -> bool:
    if type(body1) is Circle:
        if type(body2) is Circle:
            return collision_detection_between_circles(body1, body2)
        else:
            return collision_detection_between_circle_and_polygon(body1, body2)
    else:
        if type(body2) is Polygon:
            return collision_detection_between_polygons(body1, body2)
        else:
            return collision_detection_between_circle_and_polygon(body2, body1)
    pass
