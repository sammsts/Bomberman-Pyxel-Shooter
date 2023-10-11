import pyxel
from math import sqrt

x, y = 90, 10
radius = 5
velocity = 1

def update():
    global y, velocity
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        dx = pyxel.mouse_x - x
        dy = pyxel.mouse_y - y
        
        if sqrt(dx**2 + dy**2) < radius:
            velocity = 0

    y += velocity

def draw():
    pyxel.cls(pyxel.COLOR_BLACK)
    color = pyxel.COLOR_WHITE

    if velocity == 0:
        color = pyxel.COLOR_GREEN
        pyxel.text(70, 90, "Parabéns!", pyxel.COLOR_WHITE)
    pyxel.circ(x, y, 5, color)

pyxel.init(180, 120)
pyxel.mouse(True)
pyxel.run(update, draw)