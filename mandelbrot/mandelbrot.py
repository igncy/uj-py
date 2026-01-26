#!/usr/bin/env -S PYGAME_HIDE_SUPPORT_PROMPT= python

import colorsys
import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''

import pygame as pg


ROWS_PER_FRAME: int = 20


#TODO
# documentation; pdoc?
# numpy
# multithreading
# boundary tracing
# mouse drag
# display magnification


def colour(n: float) -> tuple[int, int, int]:
    """Return an RGB tuple based on the value of n."""
    if n == 0: return 0, 0, 0
    rgba = colorsys.hsv_to_rgb((0.5 + 1.5*n) % 1.0, 0.8, 0.9)
    return tuple(int(255 * rgba[i]) for i in range(3))


def colour2(n: float) -> tuple[int, int, int]:
    """Return an RGB tuple based on the value of n."""
    if n <= 0: return 0, 0, 0
    steps = [
        (0.0, (0, 7, 100)), # dark blue
        (0.16, (32, 107, 203)), # blue
        (0.42, (237, 255, 255)), # white
        (0.65, (255, 170, 0)), # orange
        (0.82, (181, 68, 11)),  # dark orange
        (0.85, (0, 2, 0)), # black
        (1.0, (237, 255, 255)) # white
    ]
    n = (0.7 * n) % 1.0
    for i in range(len(steps) - 1):
        n1, rgb1 = steps[i]
        n2, rgb2 = steps[i + 1]
        if n1 <= n <= n2:
            # linear interpolation y = y1 + (y2-y1) * (x-x1) / (x2-x1)
            t = (n-n1) / (n2-n1)
            return tuple(int(rgb1[j] + (rgb2[j]-rgb1[j]) * t) for j in range(3))


class App:
    def __init__(self, width=None, height=None, bound=2, max_iter=50, power=2, colour_func=colour2):
        if not pg.get_init(): pg.init()

        if not width or not height:
            display_info = pg.display.Info()
            self.width, self.height = display_info.current_w, display_info.current_h
        else:
            self.width, self.height = width, height

        self.bound = bound
        self.max_iter = max_iter
        self.power = power
        self.screen = None
        self.buffer = None
        self.running = False
        self.to_draw = True
        self.drawn_rows = 0
        self.camera_step = 0.03
        self.zoom_step = 0.05
        self.colours = [colour_func(i / max_iter) for i in range(self.max_iter + 1)]

        x_length = 3.0
        y_length = 3.0
        x_center = -0.7
        y_center = 0.0
        self.x_min = x_center - x_length/2
        self.x_max = x_center + x_length/2
        self.y_min = y_center - y_length/2
        self.y_max = y_center + y_length/2

    def __del__(self):
        pg.quit()

    def update_size(self) -> None:
        self.width, self.height = pg.display.get_surface().get_size()
        self.buffer = pg.Surface((self.width, self.height))
        self.drawn_rows = 0
        self.to_draw = True

    # def _f(self, z: complex, c: complex) -> complex:
    #     return z*z + c if self.power == 2 else z**self.power + c

    def mandelbrot(self) -> bool:
        pixels = pg.PixelArray(self.buffer)
        width, height = self.width, self.height
        x_min = self.x_min
        x_max = self.x_max
        y_min = self.y_min
        y_max = self.y_max
        max_iter = self.max_iter
        bound = self.bound
        colours = self.colours

        if self.power == 2:
            bound2 = bound * bound

            for y in range(ROWS_PER_FRAME):
                if self.drawn_rows >= height:
                    pixels.close()
                    return True
                y = self.drawn_rows
                y_ = y_min + (y_max-y_min) * y / (height-1)
                for x in range(width):
                    x_ = x_min + (x_max-x_min) * x / (width-1)
                    # z = 0 + 0j
                    # c = complex(x_, y_)
                    # c = x_ + 1j*y_
                    zr = zi = 0.0
                    for i in range(max_iter):
                        zr2 = zr * zr
                        zi2 = zi * zi
                        # if abs(z) >= self.bound:
                        # if z.real*z.real + z.imag*z.imag >= self.bound*self.bound:
                        if zr2 + zi2 >= bound2:
                            iters = i
                            break
                        else:
                            # z = self._f(z, c)
                            zi = 2*zr*zi + y_
                            zr = zr2 - zi2 + x_
                    else:
                        iters = 0
                    pixels[x, y] = colours[iters]
                self.drawn_rows += 1
        else:
            power = self.power

            for y in range(ROWS_PER_FRAME):
                if self.drawn_rows >= height:
                    pixels.close()
                    return True
                y = self.drawn_rows
                y_ = y_min + (y_max-y_min) * y / (height-1)
                for x in range(width):
                    x_ = x_min + (x_max-x_min) * x / (width-1)
                    z = 0 + 0j
                    c = x_ + 1j*y_
                    for i in range(max_iter):
                        if z.real*z.real + z.imag*z.imag >= bound*bound:
                            iters = i
                            break
                        else:
                            z = z**power + c
                    else:
                        iters = 0
                    pixels[x, y] = colours[iters]
                self.drawn_rows += 1

        pixels.close()
        return False

    def draw_screen(self) -> None:
        drawn_all = self.mandelbrot()
        self.screen.blit(self.buffer, (0, 0))
        pg.display.flip()
        if drawn_all: self.to_draw = False

    def handle_keys(self, key=None) -> bool:
        dx = (self.x_max - self.x_min) * self.camera_step
        dy = (self.y_max - self.y_min) * self.camera_step
        zx = (self.x_max - self.x_min) * self.zoom_step
        zy = (self.y_max - self.y_min) * self.zoom_step

        if key:
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
        else:
            keys = pg.key.get_pressed()
            if keys[pg.K_w] or keys[pg.K_UP]:
                """Move camera up on W or Up."""
                self.y_min -= dy
                self.y_max -= dy
            if keys[pg.K_s] or keys[pg.K_DOWN]:
                """Move camera down on S or Down."""
                self.y_min += dy
                self.y_max += dy
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                """Move camera left on A or Left."""
                self.x_min -= dx
                self.x_max -= dx
            if keys[pg.K_d] or keys[pg.K_RIGHT]:
                """Move camera right on D or Right."""
                self.x_min += dx
                self.x_max += dx
            if keys[pg.K_e] or keys[pg.K_PAGEUP]:
                """Zoom in on E or Page Up."""
                self.x_min += zx
                self.x_max -= zx
                self.y_min += zy
                self.y_max -= zy
            if keys[pg.K_q] or keys[pg.K_PAGEDOWN]:
                """Zoom out on Q or Page Down."""
                self.x_min -= zx
                self.x_max += zx
                self.y_min -= zy
                self.y_max += zy
            else:
                return True

        self.to_draw = True
        self.drawn_rows = 0
        return True

    def run(self) -> None:
        self.screen = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        self.buffer = pg.Surface((self.width, self.height))
        self.running = True
        pg.display.set_caption('Mandelbrot set')

        while self.running:
            if self.to_draw: self.draw_screen()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                    break
                if event.type == pg.KEYDOWN and not self.handle_keys(event.key):
                    self.running = False
                    break
                if any(pg.key.get_pressed()) and not self.handle_keys():
                    self.running = False
                    break
                if event.type == pg.VIDEORESIZE:
                    self.update_size()
                if event.type == pg.MOUSEWHEEL:
                    zx = (self.x_max - self.x_min) * self.zoom_step
                    zy = (self.y_max - self.y_min) * self.zoom_step
                    if event.y > 0:
                        """Zoom in on Scroll Up."""
                        self.x_min += zx
                        self.x_max -= zx
                        self.y_min += zy
                        self.y_max -= zy
                    else:
                        """Zoom out on Scroll Down."""
                        self.x_min -= zx
                        self.x_max += zx
                        self.y_min -= zy
                        self.y_max += zy
                    self.to_draw = True
                    self.drawn_rows = 0


if __name__ == '__main__':

    app = App(500, 400, 10, 50, 2, colour_func=colour2)
    app.run()
