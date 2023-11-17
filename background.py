import pyxel

STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5
NUM_STARS = 100

class Background:
    def __init__(self):
        # self.stars = []
        # for i in range(NUM_STARS):
        #     self.stars.append(
        #         (
        #             pyxel.rndi(0, pyxel.width - 1),
        #             pyxel.rndi(0, pyxel.height - 1),
        #             pyxel.rndf(1, 2.5),
        #         )
        #     )
        self.background_image = pyxel.image(0)
        self.background_image.load(0, 15, "assets/img.png")

    def update(self):
        # for i, (x, y, speed) in enumerate(self.stars):
        #     y += speed
        #     if y >= pyxel.height:
        #         y -= pyxel.height
        #     self.stars[i] = (x, y, speed)
        pass

    def draw(self):
        # for x, y, speed in self.stars:
        #     pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)
        pyxel.blt(0, 0, 0, 0, 0, pyxel.width, pyxel.height, 0)