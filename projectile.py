import pyxel
from entity import Entity

BULLET_WIDTH = 2
BULLET_HEIGHT = 8
BULLET_COLOR = 11
BULLET_SPEED = 4

bullets = []

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.x = x
        self.y = y
        self.w = BULLET_WIDTH
        self.h = BULLET_HEIGHT
        self.is_alive = True
        bullets.append(self)

    def update(self):
        try:
            self.y -= BULLET_SPEED
            if self.y + self.h - 1 < 0:
                self.is_alive = False
        except ZeroDivisionError as e:
            print(f"Erro ao atualizar bala: {e}")

    def draw(self):
        pyxel.rect(self.x, self.y, self.w, self.h, BULLET_COLOR)