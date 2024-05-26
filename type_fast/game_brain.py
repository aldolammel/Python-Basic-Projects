from tkinter import Tk, Message, Entry, Button
from stopwatch import Stopwatch
from time import sleep


class GameBrain:
    def __init__(self, wrds, t_limiter):
        self.wrds_selected = wrds
        # Window:
        self.root = Tk()
        # Fields:
        self.field_words = Message()
        self.user_input = Entry()
        # Buttons:
        self.bt_restart = Button(command=self.restart)
        # Binds:
        self.user_input.bind("<space>", self.check_word(), add="+")  # this "add='+'" means we're using more 1 key.
        self.user_input.bind("<Return>", self.check_word(), add="+")
        self.user_input.bind("<Key>", self.start_timer())  # "<Key>" means any key.
        # Timer:
        self.timer = Stopwatch(self.root, t_limiter)

    def start_timer(self):
        self.Stopwatch.start()

    def restart(self):
        self.timer.stop()
        check_word()
        sleep(3)
        self.timer.should_play = True
        start_timer()

    def check_word(self):  # "param=None" will block the necessity to call the func w/ "()", calling "check_word" only
        for w in self.wrds_selected:
            if w == self.user_input.get() and self.timer.is_t_running:
                # Remove the correct word from the list:
                self.wrds_selected.remove(w)
                print(f"Correct: {w}!")
                # Clean the field:
                self.user_input.delete(0, len(w))
                # Update the board:
                self.field_words.config(text=self.wrds_selected)
        # Check whether the game must keep is_t_running:
        self.root.after(1, self.is_there_wrd_available)

    def is_there_wrd_available(self):
        if len(self.wrds_selected) == 0:
            return False
        return True
