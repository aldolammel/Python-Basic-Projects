from db import db_en
from random import sample, shuffle
from game_brain import GameBrain
from game_ui import GameUI

# Game Setup:
wrds_database = list(db_en)
wrds_limiter = 10  # Number of words.
T_LIMITER = 60  # In seconds.

# Other definitions:
WRDS_LIMITER_MAX = len(wrds_database)
WRDS_LIMITER_MIN = 5

# Error handlers:
if WRDS_LIMITER_MIN > wrds_limiter:
    wrds_limiter = WRDS_LIMITER_MIN
    print(f"\nDEBUG >> You're playing with the minimum words amount: {wrds_limiter}\n")
elif WRDS_LIMITER_MAX < wrds_limiter:
    wrds_limiter = WRDS_LIMITER_MAX
    print(f"\nDEBUG >> You're playing with all available words: {wrds_limiter}\n")

# Building temporary database:
wrds_selected = sample(wrds_database, wrds_limiter)
shuffle(wrds_database)
print(len(wrds_selected))

game_brain = GameBrain(wrds_selected, T_LIMITER)
game_ui = GameUI(game_brain)
