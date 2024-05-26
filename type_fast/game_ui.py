from game_brain import GameBrain
from tkinter import Canvas, Label


class GameUI:

    def __init__(self, game_brain: GameBrain):
        self.game = game_brain
        # Window:
        self.game.root.title("Type Faster by @aldolammel")
        self.game.root.minsize(width=0, height=0)
        self.game.root.config(padx=20, pady=20, bg="#F1F1F1")
        # Window > Canvas:
        self.canvas = Canvas(width=400, height=300)
        self.canvas.config(highlightthickness=0, bg="#F1F1F1")
        self.canvas.grid(column=1, row=1, pady=10)
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




"""

        # TODO: if there's word available, do it:
        elif self.ui.user_input.get() == " ":
            # When it uses the space bar to start the word checking, an unwanted space is created. It'll delete that
            # but other characters:
            self.ui.user_input.delete(0)"""