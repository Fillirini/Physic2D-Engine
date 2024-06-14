import math


class Vector2:
    x: float
    y: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
        pass

    def length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def square_length(self):
        return pow(self.x, 2) + pow(self.y, 2)

    def distance(self, other):
        return (self - other).length()

    def normalize(self):
        return self / self.length()

    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y

    def cross(self, other) -> float:
        return self.x * other.y - self.y * other.x

    def to_tuple(self) -> [float, float]:
        return [self.x, self.y]

    def to_pygame_tuple(self, height_screen: float) -> [float, float]:
        return [self.x, height_screen - self.y]

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __imul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __itruediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __str__(self):
        return "x: " + self.x.__str__() + "  y: " + self.y.__str__()

    pass
