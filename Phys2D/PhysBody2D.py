from Phys2D.TypePhysBody import TypePhysBody
from Phys2D.Primitives import Shape


class PhysBody2D:
    primitives: list[Shape]
    type_phys_body: TypePhysBody

    def __init__(self, type_phys_body, primitives: list[Shape]):
        self.type_phys_body = type_phys_body
        self.primitives = primitives
        pass
    pass
