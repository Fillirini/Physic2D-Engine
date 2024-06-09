from Phys2D.Primitives.Polygon import Polygon
from Math.Vector2 import Vector2


def get_normals(poly: Polygon, storage: set[Vector2]):
    i = 0
    while i < len(poly.vertices):
        edge = poly.vertices[i] - poly.vertices[i - 1]
        perpendicular = Vector2(edge.y, -edge.x)
        normal = perpendicular.normalize()
        storage.add(normal)
        i += 1
    pass


def get_projection(poly: Polygon, axis: Vector2) -> Vector2:
    min_projection: float = axis.dot(poly.vertices[0])
    max_projection: float = min_projection

    i = 1
    while i < len(poly.vertices):
        projection = axis.dot(poly.vertices[i])
        print(projection)
        if min_projection > projection:
            min_projection = projection
        elif max_projection < projection:
            max_projection = projection
        i += 1

    return Vector2(min_projection, max_projection)


def collision_detection_between_polygons(poly1: Polygon, poly2: Polygon) -> bool:
    normals: set[Vector2] = set()

    get_normals(poly1, normals)
    get_normals(poly2, normals)

    print(len(normals))

    for normal in normals:
        projection_1 = get_projection(poly1, normal)
        projection_2 = get_projection(poly2, normal)

        if projection_1.y < projection_2.x or projection_2.y < projection_1.x:
            return False  #не пересекаются

    return True  #пересекаются
