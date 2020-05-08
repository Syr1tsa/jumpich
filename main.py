#  Джампыч
import pygame as pg
import random

from settings import *
from sprites import *

class Game:
    def __init__(self):
        #  initialize window for game
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(GAME_NAME)
        self.clock = pg.time.Clock()
        self.loop = True

    def new(self):
        #  start new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        pl = Platform(0, HEIGHT - 40, WIDTH, 40)
        self.all_sprites.add(pl)
        self.platforms.add(pl)
        p2 = Platform(WIDTH/2 - 50, HEIGHT*3/4, 100, 20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

        self.run()

    def run(self):
        #  Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        #  Game loop updating
        self.all_sprites.update()
        hits = pg.sprite.spritecollide(self.player, self.platforms, False)

        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

    def events(self):
        #  Game loop events
        for event in pg.event.get():
            #  closing window cheeck :)
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.loop = False

    def draw(self):
        #  Game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def show_start_screen(self):
        #  game start screen
        pass

    def show_go_screen(self):
        #  game continue ( start again )
        pass


g = Game()
g.show_start_screen()
while g.loop:
    g.new()
    g.show_go_screen()

pg.quit()
