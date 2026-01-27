#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

#TODO obj w/ draw(): paddle, score (or player instead of paddle+score), net?, game/window/app, ball

import os
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

import pygame as pg


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @classmethod
    # def from_tuple(cls, xy_tuple):
    #     # return cls(xy_tuple[0], xy_tuple[1])
    #     return cls(*xy_tuple)

    def tuple(self):
        return self.x, self.y


class Player:
    def __init__(self, name='Player'):
        self.name = name
        self.score = 0
        self.pos = Coordinate(0, 0)

    def draw(self):
        pass


class PlayerAI(Player):
    # def __init__(self):
    #     super().__init__(name='Computer')
    pass


class Game:
    def __init__(self, app, players: tuple[Player, Player]):
        self.app = app
        self.players = players

    def draw_net(self):
        screen = self.app.screen
        fg = self.app.FG_COLOUR
        x = self.app.WIDTH / 2
        y = 0
        margin = 15
        length = 30
        width = 20

        for y in range(margin, self.app.HEIGHT - margin - length, margin + length):
            pg.draw.line(
                screen,
                fg,
                (x, y),
                (x, y + length),
                width
            )
        y += length + margin
        pg.draw.line(
            screen,
            fg,
            (x, y),
            (x, self.app.HEIGHT - margin),
            width
        )

    def draw_scores(self):
        pass


class App:
    def __init__(self, width=None, height=None):
        if not pg.get_init(): pg.init()

        if not (width and height):
            display_info = pg.display.Info()
            self.width, self.height = display_info.current_w, display_info.current_h
        else:
            self.width = width
            self.height = height

        self.window_title = 'Pong'
        self.bg_colour = 'black'
        self.fg_colour = 'white'
        self.FPS = 30
        self.screen = None
        self.clock = None
        self.game = None
        self.running = False
        self.dt = 0

    def __del__(self):
        pg.quit()

    def draw_scanlines(self):
        scanlines = pg.Surface((self.width, self.height)).convert_alpha()
        for i in range(0, self.height, 3):
            scanlines.fill((0, 0, 0, 100), (0, i, self.width, 1))
        self.screen.blit(scanlines, self.screen.get_rect())

    def draw_frame(self, to_draw):
        self.screen.fill(self.bg_colour)

        self.game.draw_net()
        self.draw_scanlines()

        for f in to_draw: f()

        pg.display.flip()
        self.dt = self.clock.tick(self.FPS) / 1000

    @staticmethod
    def handle_key(key) -> bool:
        # if key == pg.K_q:
        #     return False
        match key:
            case pg.K_q:
                return False
        return True

    def start(self, two_players=False):
        self.game = Game(self, (
            Player('Player 1'),
            PlayerAI('Player 2') if two_players else Player('Player 2')
        ))
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.running = True
        pg.display.set_caption(self.window_title)
        to_draw = (
            self.game.draw_net,
            self.game.draw_scores,
            *(player.draw for player in self.game.players),
            self.draw_scanlines
        )

        while self.running:
            self.width, self.height = pg.display.get_surface().get_size()

            self.draw_frame(to_draw)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    break
                if event.type == pg.KEYDOWN:
                    if not self.handle_key(event.key):
                    # if not App.handle_key(event.key):
                        self.running = False
                        break


if __name__ == '__main__':

    game = App(1280, 720)

    if len(sys.argv) > 1 and sys.argv[1] in ('--2', '-2'):
        game.start(two_players=True)
    else:
        game.start()
