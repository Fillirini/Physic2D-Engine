import pygame as pg
from Phys2D.World import World
from Phys2D.Primitives import *
from Math.Vector2 import Vector2
from Phys2D.CollisionDetection.сollision_detection import check_collision

pg.init()
screen = pg.display.set_mode((1080, 720))

world = World()
circle = Circle(Vector2(520, 380), 76)

hex_vertices = [Vector2(500, 500), Vector2(650, 575), Vector2(650, 650), Vector2(500, 700), Vector2(450, 650), Vector2(450, 575)]
hexagon = Polygon(Vector2(780, 467), hex_vertices)

vertices = [Vector2(100, 0), Vector2(50, 50), Vector2(75, 100), Vector2(150, 75), Vector2(200, 0)]
pentagon = Polygon(Vector2(100, 100), vertices)

color = [255, 255, 255]
color2 = [255, 255, 255]
color3 = [255, 255, 255]

def phys2Dvector_to_pygamevector(vectors: list[Vector2]) -> list[pg.Vector2]:
    l = list()
    for vector in vectors:
        l.append(pg.Vector2(vector.x, vector.y))
    return l


clock = pg.time.Clock()
run = True
while run:
    screen.fill((0, 0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    keys = pg.key.get_pressed()
    if keys[pg.K_a]:
        pentagon.move(Vector2(-5, 0))
    if keys[pg.K_d]:
        pentagon.move(Vector2(5, 0))
    if keys[pg.K_w]:
        pentagon.move(Vector2(0, -5))
    if keys[pg.K_s]:
        pentagon.move(Vector2(0, 5))

    if check_collision(pentagon, circle):
        color = [255, 0, 0]
        color3 = [255, 0, 0]
    else:
        color = [255, 255, 255]
        color3 = [255, 255, 255]

    if check_collision(pentagon, hexagon):
        color2 = [255, 0, 0]
        color3 = [255, 0, 0]
    else:
        color2 = [255, 255, 255]
        if color3 != [255, 0, 0]:
            color3 = [255, 255, 255]

    pg.draw.polygon(screen, color3, phys2Dvector_to_pygamevector(pentagon.vertices), 2)
    pg.draw.polygon(screen, color2, phys2Dvector_to_pygamevector(hexagon.vertices), 2)
    pg.draw.circle(screen, color, (circle.position.x, circle.position.y), circle.radius, 2)
    pg.display.flip()
    clock.tick(30.0)

pg.quit()
