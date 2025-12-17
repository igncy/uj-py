#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

import os
import sys

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

import pygame


class Player:
    def __init__(self, name='Player'):
        self.name = name

    def draw(self):
        pass


class PlayerAI(Player):
    def __init__(self):
        super().__init__(name='Computer')


class Game:
    def __init__(self, app):
        self.app = app
        self.players = []

    def draw_net(self):
        screen = self.app.screen
        fg = self.app.FG_COLOUR
        width = 10

        pygame.draw.line(
            screen,
            fg,
            (self.app.WIDTH/2, 50),
            (self.app.WIDTH/2, 100),
            width
        )

    def draw_score(self):
        pass


class App:
    def __init__(self, width=1280, height=720):
        self.WIDTH = width
        self.HEIGHT = height

        self.FPS = 30

        self.BG_COLOUR = 'black'
        self.FG_COLOUR = 'white'

        self.screen = None
        self.clock = None

        pygame.init()

        self.game = None

        self.running = False
        self.dt = 0

    def draw_frame(self):
        self.screen.fill(self.BG_COLOUR)

        self.game.draw_net()

        pygame.display.flip()
        self.dt = self.clock.tick(self.FPS) / 1000

    def start(self):
        self.game = Game(self)

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('pong')

        self.running = True

        while self.running:
            self.WIDTH, self.HEIGHT = pygame.display.get_surface().get_size()

            self.draw_frame()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                if event.type == pygame.KEYDOWN:
                    pass


if __name__ == '__main__':

    game = App()

    if len(sys.argv) > 1 and sys.argv[1] in ('--2', '-2'):
        game.start()
    else:
        game.start()