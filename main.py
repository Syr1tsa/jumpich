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

        self.player = Player(self)
        self.all_sprites.add(self.player)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

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
        #  check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        #  if player reaches top 1/4 of screen
        if self.player.rect.top <= HEIGHT/4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT:
                    plat.kill()

        #  spawn new platforms
        while len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platform(random.randrange(0, WIDTH - width),
                         random.randrange(-75, -30),
                         width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)

    def events(self):
        #  Game loop events
        for event in pg.event.get():
            #  closing window cheeck :)
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.loop = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

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
