import pyxel
from entity import Entity
from projectile import Bullet, BULLET_WIDTH, BULLET_HEIGHT

PLAYER_WIDTH = 8
PLAYER_HEIGHT = 8
PLAYER_SPEED = 2

class Player(Entity):
    def __init__(self, x, y, max_hp):
        super().__init__(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.x = x
        self.y = y
        self.w = PLAYER_WIDTH
        self.h = PLAYER_HEIGHT
        self.max_hp = max_hp
        self.hp = max_hp
        self.is_alive = True

    def update(self):
        try:
            if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
                self.x -= PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
                self.x += PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
                self.y -= PLAYER_SPEED
            if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
                self.y += PLAYER_SPEED
            self.x = max(self.x, 0)
            self.x = min(self.x, pyxel.width - self.w)
            self.y = max(self.y, 0)
            self.y = min(self.y, pyxel.height - self.h)

            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
                Bullet(
                    self.x + (PLAYER_WIDTH - BULLET_WIDTH) / 2, self.y - BULLET_HEIGHT / 2
                )
                pyxel.play(3, 0)
        except IndexError as e:
            print(f"Erro ao atualizar o jogador: {e}")

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, self.w, self.h, 0)