from tkinter import *
from time import time as t
from game_ui import GameUI


class Stopwatch:
    def __init__(self, root, t_limiter):
        self.root = root
        self.display = "00:00.000"
        self.t_limiter = t_limiter
        self.lb_t_display = Label(
            root,
            text=self.display,
            font=("Arial", 28)
        )
        self.lb_t_display.grid(column=1, row=3)
        self.start_t = None
        self.is_t_running = False
        self.should_play = True
        self.update_display()

    def start(self):
        if not self.is_t_running and self.should_play:
            self.start_t = t()
            self.is_t_running = True
            self.update_display()

    def update_display(self):
        if self.is_t_running:
            t_elapsed = int((t() - self.start_t) * 1000)
            t_limiter = self.t_limiter * 1000  # X seconds in milliseconds
            # If timeout:
            if t_elapsed >= t_limiter:
                self.stop()
                t_elapsed = t_limiter

            min_ = (t_elapsed // 60000) % 60
            sec_ = (t_elapsed // 1000) % 60
            mil_ = t_elapsed % 1000
            self.lb_t_display.config(text=f"{min_:02}:{sec_:02}.{mil_:03}")

            if self.is_t_running:
                self.root.after(10, self.update_display)
        # else:
            # self.lb_t_display.config(text=self.display)

    def stop(self):
        self.is_t_running = False
        self.should_play = False
        GameUI.lb_title.config(text="The game's over!")
        GameUI.user_input.config(state="disabled")
        print("\n>> The game's over!\n")
