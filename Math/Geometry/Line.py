from Math import Vector2


class Line:
    start: Vector2
    end: Vector2

    def __init__(self, start, end):
        self.start = start
        self.end = end
        pass

    def get_edge(self) -> Vector2:
        return self.end - self.start

    pass
