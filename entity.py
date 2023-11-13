class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_alive = True

    def update(self):
        pass  # Lógica de atualização genérica para entidades

    def draw(self):
        pass  # Lógica de desenho genérica para entidades