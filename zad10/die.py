#!/usr/bin/env python

import random
import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg='black')
        self.root.title('Dice roll')
        self.root.geometry('180x150')
        self.root.resizable(False, False)
        self.value = tk.StringVar(value=" ")
        self.colors = [
            'yellow',
            'orange',
            'red',
            'lime green',
            'cyan',
            'magenta',
        ]

        self.label = tk.Label(
            self.root,
            textvariable=self.value,
            font=('Cascadia Mono', 50, 'bold'),
            fg='white',
            bg='black',
        )
        self.label.pack()

        button = tk.Button(
            self.root,
            text='ROLL',
            font=('Cascadia Mono', 15),
            fg='white',
            bg='black',
            activebackground='#2e2e2e',
            activeforeground='white',
            cursor='hand2',
            highlightthickness=0,
            borderwidth=0,
            command=self.roll
        )
        button.pack()

    def roll(self):
        n = random.randrange(1, 7)
        self.value.set(str(n))
        self.label.config(fg=self.colors[n-1])

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':

    app = App()
    app.run()
