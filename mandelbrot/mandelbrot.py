#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

import colorsys
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''; import pygame as pg

#TODO pdoc

def colour(n):
    if n == 0: return 0, 0, 0
    return tuple(map(lambda x: int(255 * x), colorsys.hsv_to_rgb(0.95 * n, 0.8, 1.0)))


class App:
    def __init__(self, width=None, height=None, bound=2, max_iter=50, power=2):
        if not pg.get_init(): pg.init()

        if not width or not height:
            display_info = pg.display.Info()
            self.width, self.height = display_info.current_w, display_info.current_h
        else:
            self.width, self.height = width, height

        self.bound = bound
        self.max_iter = max_iter
        self.power = power
        pg.display.set_caption('Mandelbrot set')
        self.bg_colour = 'black'
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.temp_surface = pg.Surface((self.width, self.height), pg.RESIZABLE)
        self.pixels = None
        self.running = False
        self.to_draw = True
        self.colours = [pg.Color(colour(i/max_iter)) for i in range(self.max_iter+1)]
        x_length = 3.0
        y_length = 3.0
        x_center = -0.7
        y_center = 0.0
        self.x_min = x_center - x_length/2
        self.x_max = x_center + x_length/2
        self.y_min = y_center - y_length/2
        self.y_max = y_center + y_length/2
        self.camera_step = 0.1
        self.zoom_step = 0.1

    def __del__(self):
        pg.quit()

    def update_size(self):
        self.width, self.height = pg.display.get_surface().get_size()

    def _f(self, z, c):
        return z*z + c if self.power == 2 else z**self.power + c

    def mandelbrot(self, width, height):
        pixels = pg.PixelArray(self.temp_surface)

        for y in range(height):
            pg.event.pump()
            y_ = self.y_min + (self.y_max-self.y_min) * y / (height-1)
            for x in range(width):
                x_ = self.x_min + (self.x_max-self.x_min) * x / (width-1)
                z = 0
                c = complex(x_, y_)
                for i in range(self.max_iter):
                    # if abs(z) >= self.bound:
                    if z.real*z.real + z.imag*z.imag >= self.bound*self.bound:
                        iters = i
                        break
                    else:
                        z = self._f(z, c)
                else:
                    iters = 0
                pixels[x, y] = self.colours[iters]

        pixels.close()

    def draw_screen(self):
        self.mandelbrot(self.width, self.height)
        self.screen.blit(self.temp_surface, (self.x_min, self.y_min))
        pg.display.flip()

    def handle_key(self, key) -> bool:
        dx = (self.x_max-self.x_min) * self.camera_step
        dy = (self.y_max-self.y_min) * self.camera_step
        zx = (self.x_max-self.x_min) * self.zoom_step
        zy = (self.y_max-self.y_min) * self.zoom_step

        match key:
            case pg.K_ESCAPE:
                """Quit on Escape."""
                return False
            case pg.K_w | pg.K_UP:
                """Move camera up on W or Up."""
                self.y_min -= dy
                self.y_max -= dy
            case pg.K_s | pg.K_DOWN:
                """Move camera down on S or Down."""
                self.y_min += dy
                self.y_max += dy
            case pg.K_a | pg.K_LEFT:
                """Move camera left on A or Left."""
                self.x_min -= dx
                self.x_max -= dx
            case pg.K_d | pg.K_RIGHT:
                """Move camera right on D or Right."""
                self.x_min += dx
                self.x_max += dx
            case pg.K_e | pg.K_PAGEUP:
                """Zoom in on E or Page Up."""
                self.x_min += zx
                self.x_max -= zx
                self.y_min += zy
                self.y_max -= zy
            case pg.K_q | pg.K_PAGEDOWN:
                """Zoom out on Q or Page Down."""
                self.x_min -= zx
                self.x_max += zx
                self.y_min -= zy
                self.y_max += zy
            case _:
                return True

        self.to_draw = True
        return True

    def run(self):
        self.running = True
        while self.running:
            self.update_size()

            if self.to_draw:
                self.draw_screen()
                self.to_draw = False

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    break
                if event.type == pg.KEYDOWN:
                    if not self.handle_key(event.key):
                        self.running = False
                        break
                if event.type == pg.VIDEORESIZE:
                    self.update_size()
                    self.to_draw = True


if __name__ == '__main__':

    app = App(700, 600, 2, 50, 2)
    app.run()
