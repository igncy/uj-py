#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

import colorsys
import os
# import numpy as np
# import matplotlib.pyplot as plot
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''; import pygame as pg

#TODO pdoc

def colour(t):
    if t == 0: return 0, 0, 0
    r, g, b = colorsys.hsv_to_rgb(0.95 * t, 0.8, 1.0)
    return int(r * 255), int(g * 255), int(b * 255)
    # return tuple(map(lambda x: int(x * 255), colorsys.hsv_to_rgb(0.95 * t, 0.8, 1.0)))


def colour2(t):
    return (
        int(255 * t ** 1),
        int(50 * t ** 1.2),
        int(255 * t ** .8)
    )


class Mandelbrot:
    pass


class App:
    def __init__(self, width=None, height=None):
        if not pg.get_init(): pg.init()

        if not width or not height:
            display_info = pg.display.Info()
            self.WIDTH, self.HEIGHT = display_info.current_w, display_info.current_h
        else:
            self.WIDTH, self.HEIGHT = width, height

        self.WINDOW_TITLE = 'Mandelbrot set'
        self.BG_COLOUR = 'black'
        self.FPS = 24
        self.screen = None
        self.clock = None
        self.running = False
        self.dt = 0

        # self.xs = np.linspace(-1.5, .5, 300)
        # self.ys = np.linspace(-1, 1, 300)

        self.BOUND = 2
        self.MAX_ITER = 50

        aspect = self.WIDTH / self.HEIGHT
        x_width = 3.5
        y_height = x_width / aspect
        x_center = -0.75
        y_center = 0
        self.x_min = x_center - x_width / 2
        self.x_max = x_center + x_width / 2
        self.y_min = y_center - y_height / 2
        self.y_max = y_center + y_height / 2

        # self.x_min, self.x_max = -2.5, 1.0
        # self.y_min, self.y_max = -1.0, 1.0
        self.zoom_factor = 0.8
        self.pan_step = 0.1

        self.run()

    def __del__(self):
        pg.quit()

    def update_size(self):
        self.WIDTH, self.HEIGHT = pg.display.get_surface().get_size()

    # @staticmethod
    # def mandelbrot(xs, ys):
    #     bound = 2
    #     max_iter = 20
    #     iters = []
    #     for y in ys:
    #         row = []
    #         for x in xs:
    #             z = 0
    #             c = complex(x, y)
    #             for i in range(max_iter):
    #                 if abs(z) >= bound:
    #                     row.append(i)
    #                     break
    #                 else:
    #                     z = z * z + c
    #             else:
    #                 row.append(0)
    #         iters.append(row)
    #     return iters
    #
    # @staticmethod
    # def plot_mandelbrot(xs, ys, iters):
    #     axes = plot.axes()
    #     axes.set_aspect('equal')
    #     graph = axes.pcolormesh(xs, ys, iters)
    #     plot.colorbar(graph)
    #     plot.show()

    def mandelbrot(self, width, height):
        for y in range(height):
            # y_ = -1 + 2 * float(y) / (height - 1)
            y_ = self.y_min + (self.y_max - self.y_min) * float(y) / (width - 1)
            for x in range(width):
                # x_ = -2.5 + 3.5 * float(x) / (width - 1)
                x_ = self.x_min + (self.x_max - self.x_min) * float(x) / (height - 1)
                z = 0
                c = complex(x_, y_)
                for i in range(self.MAX_ITER):
                    if abs(z) >= self.BOUND:
                        t = i
                        break
                    else:
                        z = z * z + c
                else:
                    t = 0
                self.screen.set_at((x, y), colour(t / self.MAX_ITER))

    def draw_frame(self):
        self.screen.fill(self.BG_COLOUR)

        self.mandelbrot(self.WIDTH, self.HEIGHT)

        pg.display.flip()
        self.dt = self.clock.tick(self.FPS) / 1000

    @staticmethod
    def handle_key(key) -> bool:
        match key:
            case pg.K_q | pg.K_ESCAPE:
                return False
        return True

    def run(self):
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.RESIZABLE)
        self.clock = pg.time.Clock()
        self.running = True
        pg.display.set_caption(self.WINDOW_TITLE)

        while self.running:
            self.update_size()

            self.draw_frame()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    break
                if event.type == pg.KEYDOWN:
                    if not self.handle_key(event.key):
                        self.running = False
                        break


if __name__ == '__main__':

    app = App(800, 650)
