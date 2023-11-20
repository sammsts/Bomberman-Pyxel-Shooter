class Entity:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_alive = True

    def update(self):
        pass 

    def draw(self):
        pass