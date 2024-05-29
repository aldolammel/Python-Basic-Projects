from random import sample, shuffle


class GameBrain:
    def __init__(self, wrds, wrds_limiter):
        self.wrds = wrds
        self.wrds_limiter = wrds_limiter
        self.wrds_selected = "Click 'New Game' to receive the words to type."
        self.wrds_selected_bkp = list()
        # Managers:
        self.was_played = False
        self.is_t_running = False
        self.was_restarted = False
        self.was_timeout = False
        # Others:
        self.last_display_num = ""

    def select_new_wrds(self):
        wrds_selected = sample(self.wrds, self.wrds_limiter)
        shuffle(wrds_selected)
        self.wrds_selected = wrds_selected.copy()
        self.wrds_selected_bkp = wrds_selected.copy()

    def should_play(self):
        if len(self.wrds_selected) > 0:
            return True
        return False
