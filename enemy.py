import pyxel
from entity import Entity

ENEMY_WIDTH = 8
ENEMY_HEIGHT = 8
ENEMY_SPEED = 1.5

enemies = []

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.x = x
        self.y = y
        self.w = ENEMY_WIDTH
        self.h = ENEMY_HEIGHT
        self.dir = 1
        self.timer_offset = pyxel.rndi(0, 59)
        self.is_alive = True
        enemies.append(self)

    def update(self):
        try:
            if (pyxel.frame_count + self.timer_offset) % 60 < 30:
                self.x += ENEMY_SPEED
                self.dir = 1
            else:
                self.x -= ENEMY_SPEED
                self.dir = -1
            self.y += ENEMY_SPEED
            if self.y > pyxel.height - 1:
                self.is_alive = False
        except Exception as e:
            print(f"Erro ao atualizar inimigo: {e}")

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 8, 0, self.w * self.dir, self.h, 0)