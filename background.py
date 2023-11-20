import pyxel

STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5
NUM_STARS = 100

class Background:
    def __init__(self):
        self.background_image = pyxel.image(0)
        self.background_image.load(0, 15, "assets/img.png")

    def update(self):
        pass

    def draw(self):
        pyxel.blt(0, 0, 0, 0, 0, pyxel.width, pyxel.height, 0)