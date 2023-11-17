import pyxel
from player import Player, PLAYER_WIDTH, PLAYER_HEIGHT
from background import Background
from enemy import Enemy, ENEMY_WIDTH, ENEMY_HEIGHT, enemies
from blast import Blast, blasts
from projectile import bullets

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2

def update_list(list):
    for elem in list:
        elem.update()


def draw_list(list):
    for elem in list:
        elem.draw()


def cleanup_list(list):
    i = 0
    while i < len(list):
        elem = list[i]
        if not elem.is_alive:
            list.pop(i)
        else:
            i += 1


def load_bgm(msc, filename, snd1, snd2, snd3):
    #Loads a json file for 8bit BGM generator by frenchbread.
    #Each track is stored in snd1, snd2 and snd3 of the sound
    #respectively and registered in msd of the music.
    import json

    with open(filename, "rt") as file:
        bgm = json.loads(file.read())
        pyxel.sound(snd1).set(*bgm[0])
        pyxel.sound(snd2).set(*bgm[1])
        pyxel.sound(snd3).set(*bgm[2])
        pyxel.music(msc).set([snd1], [snd2], [snd3], [])

class App:
    def __init__(self):
        pyxel.init(120, 160, title="Bomberman Pyxel Shooter")
        pyxel.image(0).set(
            0,
            0,
            [
                "00c00c00",
                "0c7007c0",
                "0c7007c0",
                "c703b07c",
                "77033077",
                "785cc587",
                "85c77c58",
                "0c0880c0",
            ],
        )
        pyxel.image(0).set(
            8,
            0,
            [
                "00088000",
                "00ee1200",
                "08e2b180",
                "02882820",
                "00222200",
                "00012280",
                "08208008",
                "80008000",
            ],
        )
        pyxel.sound(0).set("a3a2c1a1", "p", "7", "s", 5)
        pyxel.sound(1).set("a3a2c2c2", "n", "7742", "s", 10)
        load_bgm(0, "assets/bgm_title.json", 2, 3, 4)
        load_bgm(1, "assets/bgm_play.json", 5, 6, 7)
        pyxel.load("style.pyxres")
        self.background = Background()
        self.scene = SCENE_TITLE
        self.score = 0
        self.kills = 0
        self.player = Player(pyxel.width / 2, pyxel.height - 20, max_hp = 100)
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        self.background.update()
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene == SCENE_GAMEOVER:
            self.update_gameover_scene()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_PLAY
            pyxel.playm(1, loop=True)

    def update_play_scene(self):
        if pyxel.frame_count % 6 == 0:
            Enemy(pyxel.rndi(0, pyxel.width - ENEMY_WIDTH), 0)

        for enemy in enemies:
            for bullet in bullets:
                if self.kills % 15 == 0 and self.kills > 0:
                    self.score += 30

                if (
                    enemy.x + enemy.w > bullet.x
                    and bullet.x + bullet.w > enemy.x
                    and enemy.y + enemy.h > bullet.y
                    and bullet.y + bullet.h > enemy.y
                ):
                    enemy.is_alive = False
                    bullet.is_alive = False
                    blasts.append(
                        Blast(enemy.x + ENEMY_WIDTH / 2, enemy.y + ENEMY_HEIGHT / 2)
                    )
                    pyxel.play(3, 1)
                    self.score += 5
                    self.kills += 1

        for enemy in enemies:
            if (
                self.player.x + self.player.w > enemy.x
                and enemy.x + enemy.w > self.player.x
                and self.player.y + self.player.h > enemy.y
                and enemy.y + enemy.h > self.player.y
            ):
                enemy.is_alive = False
                blasts.append(
                    Blast(
                        self.player.x + PLAYER_WIDTH / 2,
                        self.player.y + PLAYER_HEIGHT / 2,
                    )
                )
                pyxel.play(3, 1)
                self.player.hp -= 10
                if self.player.hp <= 0:
                    self.scene = SCENE_GAMEOVER
                    pyxel.playm(0, loop=True)

        self.player.update()
        update_list(bullets)
        update_list(enemies)
        update_list(blasts)
        cleanup_list(enemies)
        cleanup_list(bullets)
        cleanup_list(blasts)

    def update_gameover_scene(self):
        update_list(bullets)
        update_list(enemies)
        update_list(blasts)
        cleanup_list(enemies)
        cleanup_list(bullets)
        cleanup_list(blasts)

        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):
            self.scene = SCENE_PLAY
            self.player.x = pyxel.width / 2
            self.player.y = pyxel.height - 20
            self.score = 0
            self.kills = 0
            self.player.hp = self.player.max_hp
            enemies.clear()
            bullets.clear()
            blasts.clear()
            pyxel.playm(1, loop=True)

    def draw(self):
        pyxel.cls(0)
        self.background.draw()
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
            self.draw_ui()
        elif self.scene == SCENE_GAMEOVER:
            self.draw_gameover_scene()
            self.draw_ui()

    def draw_title_scene(self):
        pyxel.text(15, 66, "Bomberman Pyxel Shooter", pyxel.frame_count % 16)
        pyxel.text(31, 126, "- PRESS ENTER -", 13)

    def draw_play_scene(self):
        self.player.draw()
        draw_list(bullets)
        draw_list(enemies)
        draw_list(blasts)

    def draw_gameover_scene(self):
        draw_list(bullets)
        draw_list(enemies)
        draw_list(blasts)
        pyxel.text(43, 66, "GAME OVER", 8)
        pyxel.text(31, 126, "- PRESS ENTER -", 13)

    def draw_ui(self):
        pyxel.rect(0, 0, pyxel.width, 16, 3)
        pyxel.text(10, 5, f"Health: {self.player.hp}/{self.player.max_hp}", 7)
        pyxel.text(15, 17, f"SCORE {self.score:2}", 7)
        pyxel.text(70, 17, f"KILLS {self.kills:2}", 7)

        #Life bar
        health_ratio = self.player.hp / self.player.max_hp
        bar_width = int(100 * health_ratio)

        if health_ratio > 0.6:
            bar_color = 11 #Green
        elif health_ratio > 0.3:
            bar_color = 9  #Yellow
        else:
            bar_color = 8  #Red

        pyxel.rect(10, 11, bar_width, 5, bar_color) 

App()