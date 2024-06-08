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

    def dot(vector1, vector2) -> float:
        return (vector1.get_length()) * (vector2.get_length())



    def __abs__(self):
        return Vector2(abs(self.x), abs(self.y))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2(self.x / other, self.y / other)

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __lt__(self, other):
        if self.get_length() < other.get_length():
            return True
        else:
            return False

    def __gt__(self, other):
        if self.get_length() > other.get_length():
            return True
        else:
            return False

    def __le__(self, other):
        if self.get_length() <= other.get_length():
            return True
        else:
            return False

    def __ge__(self, other):
        if self.get_length() >= other.get_length():
            return True
        else:
            return False

    def __str__(self):
        return "x: " + self.x.__str__() + " y: " + self.y.__str__()

    pass
