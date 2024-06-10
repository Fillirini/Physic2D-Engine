import math


class Vector2:
    x: float
    y: float

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y
        pass



    def get_length(self) -> float:
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def normalize(self):
        return self / self.get_length()

    def dot(self, vector2) -> float:
        return self.x*vector2.x + self.y*vector2.y

    def distance(self, vector2) -> float:
        return (self - vector2).get_length()

    def is_overlap(self, vector2):
        return not (self.y < vector2.x or vector2.y < self.x)

    def get_overlap(self, vector2) -> float:
        return self.y - vector2.x

    def to_tuple(self):
        return [self.x, self.y]



    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __lt__(self, other):
        return self.get_length() < other.get_length()

    def __gt__(self, other):
        return self.get_length() > other.get_length()

    def __le__(self, other):
        return self.get_length() <= other.get_length()

    def __ge__(self, other):
        return self.get_length() >= other.get_length()

    def __str__(self):
        return "x: " + self.x.__str__() + " y: " + self.y.__str__()

    pass
