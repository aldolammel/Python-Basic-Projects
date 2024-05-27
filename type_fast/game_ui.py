from game_brain import GameBrain
from tkinter import Canvas, Label
from time import time


class GameUI:

    def __init__(self, game_brain: GameBrain, t_limiter):
        self.game = game_brain
        # Window:
        self.game.root.title("Type Faster by @aldolammel")
        self.game.root.minsize(width=0, height=0)
        self.game.root.config(padx=20, pady=20, bg="#F1F1F1")
        # Window > Canvas:
        self.canvas = Canvas(width=400, height=300)
        self.canvas.config(highlightthickness=0, bg="#F1F1F1")
        self.canvas.grid(column=1, row=1, pady=10)
        # Timer:
        self.display = "00:00.000"
        self.t_limiter = t_limiter
        self.lb_t_display = Label(
            self.game.root,
            text=self.display,
            font=("Arial", 28)
        )
        self.lb_t_display.grid(column=1, row=3)
        self.start_t = None
        self.is_t_running = False
        self.should_play = True
        self.update_display()
        # Window > Label:
        self.lb_title = Label(
            text="Type these words:",
            font=("Arial", 14, 'bold'),
            fg="#000000",
            # bg="#FFFFFF"
        )
        self.lb_title.grid(column=1, row=0)
        # Window > Fields:
        self.game.field_words.config(
            text=self.game.wrds_selected,
            font=("Arial", 12, 'bold'),
            fg="#000000",
            # bg="#FFFFFF"
        )
        self.game.field_words.grid(column=1, row=1)
        self.game.user_input.config(
            width=20,
            font=("Arial", 12),
            fg="#000000",
            bg="#FFFFFF"
        )
        self.game.user_input.grid(column=1, row=2)
        # Buttons:
        self.game.bt_restart.config(
            text="Restart",
            font=("Arial", 12),
            fg="#000000",
            # bg=""
        )
        self.game.bt_restart.grid(column=1, row=5)
        # keep the Tkinter window on screen:
        self.game.root.mainloop()

    def start(self):
        if not self.is_t_running and self.should_play:
            self.start_t = time()
            self.is_t_running = True
            self.update_display()

    def stop(self):
        self.is_t_running = False
        self.should_play = False
        self.lb_title.config(text="The game's over!")
        self.game.user_input.config(state="disabled")
        print("\n>> The game's over!\n")

    def update_display(self):
        if self.is_t_running:
            t_elapsed = int((time() - self.start_t) * 1000)
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
                self.game.root.after(10, self.update_display)
        # else:
            # self.lb_t_display.config(text=self.display)


"""
        # TODO: if there's word available, do it:
        elif self.ui.user_input.get() == " ":
            # When it uses the space bar to start the word checking, an unwanted space is created. It'll delete that
            # but other characters:
            self.ui.user_input.delete(0)
            
"""