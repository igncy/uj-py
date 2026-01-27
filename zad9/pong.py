#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

import os
import random
import sys
from enum import Enum

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

import pygame as pg


FPS = 30
PADDLE_X = 25
PADDLE_SIZE = (20, 120)
PADDLE_SPEED = 300
BALL_RADIUS = 25
BALL_SPEED = 350
MAX_SCORE = 11


class Side(Enum):
    LEFT = 0
    RIGHT = 1


class Player:
    def __init__(self, game: 'Game', side: Side):
        self.game = game
        self.side = side
        self.rect = pg.Rect(
            PADDLE_X if side == Side.LEFT else game.width - PADDLE_X - PADDLE_SIZE[0],
            game.height//2 - PADDLE_SIZE[1],
            PADDLE_SIZE[0], PADDLE_SIZE[1])
        self.score = 0
        self.name = f'Player {side.value + 1}'

    def update(self, dy):
        self.rect.y += dy * PADDLE_SPEED * self.game.dt
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > self.game.height - self.rect.height:
            self.rect.y = self.game.height - self.rect.height

    def draw(self):
        pg.draw.rect(self.game.screen, self.game.fg_colour, self.rect)


class Ball:
    def __init__(self, game):
        self.game = game
        self.rect = pg.Rect(
            game.width//2 - BALL_RADIUS//2,
            game.height//2 - BALL_RADIUS//2,
            BALL_RADIUS, BALL_RADIUS)
        self.velocity = pg.Vector2(BALL_SPEED, BALL_SPEED)
        self.reset()

    def reset(self):
        self.rect.center = (game.width//2, game.height//2)
        self.velocity = pg.Vector2(BALL_SPEED, BALL_SPEED).rotate(random.randrange(361))

    def update(self, players):
        self.rect.x += self.velocity.x * self.game.dt
        self.rect.y += self.velocity.y * self.game.dt

        if self.rect.left < 0:
            self.reset()
            players[Side.RIGHT.value].score += 1
            return
        if self.rect.right > game.width:
            self.reset()
            players[Side.LEFT.value].score += 1
            return

        if self.rect.top <= 0 or self.rect.bottom >= game.height:
            self.velocity.y *= -1
            return

        for player in players:
            if self.rect.colliderect(player.rect):
                self.velocity.x *= -1
                return

    def draw(self):
        pg.draw.circle(game.screen, self.game.fg_colour, self.rect.center, BALL_RADIUS/2)


class Game:
    def __init__(self, width=None, height=None):
        if not pg.get_init(): pg.init()

        if not (width and height):
            display_info = pg.display.Info()
            self.width, self.height = display_info.current_w, display_info.current_h
        else:
            self.width = width
            self.height = height

        self.bg_colour = 'black'
        self.fg_colour = 'white'
        self.screen = None
        self.clock = None
        self.running = False
        self.dt = 0

    def __del__(self):
        pg.quit()

    def draw_frame(self, to_draw):
        self.screen.fill(self.bg_colour)
        for obj in to_draw: obj.draw()
        pg.display.flip()
        self.dt = self.clock.tick(FPS) / 1000

    def start(self, ai=False):
        self.screen = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()
        self.running = True
        drawables = (
            *(players := (Player(self, Side.LEFT), Player(self, Side.RIGHT))),
            ball := Ball(self)
        )
        left_player = players[Side.LEFT.value]
        right_player = players[Side.RIGHT.value]
        winner = None

        while self.running:
            self.draw_frame(drawables)

            if winner:
                pg.display.set_caption(f'{winner.name} wins!')
            else:
                pg.display.set_caption(f'[{left_player.name}] {left_player.score} vs {right_player.score} [{right_player.name}]')

            for event in pg.event.get():
                if (event.type == pg.QUIT
                        or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE)):
                    self.running = False
                    break
            else:
                if not winner:
                    keys = pg.key.get_pressed()
                    for player in players:
                        if player.score >= MAX_SCORE:
                            winner = player
                            break
                        if ai and player.side == Side.LEFT:
                            continue
                        if player.side == Side.LEFT:
                            key_up = pg.K_w
                            key_down = pg.K_s
                        else:
                            key_up = pg.K_UP
                            key_down = pg.K_DOWN
                        player.update(keys[key_down] - keys[key_up])
                    else:
                        if ai:
                            t = 15
                            if -t < left_player.rect.centery - ball.rect.centery < t:
                                dy = 0
                            elif left_player.rect.centery < ball.rect.centery:
                                dy = 1
                            else:
                                dy = -1
                            left_player.update(dy)
                        ball.update(players)


if __name__ == '__main__':

    game = Game(1000, 600)

    if len(sys.argv) > 1 and '2' in sys.argv[1]:
        game.start()
    else:
        game.start(ai=True)
