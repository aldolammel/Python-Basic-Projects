from db import db_en
from random import sample, shuffle
from game_brain import GameBrain
from game_ui import GameUI

# Game Setup:
wrds_db = list(db_en)
wrds_limiter = 10  # Number of words.
T_LIMITER = 60  # In seconds.

# Other definitions:
WRDS_LIMITER_MAX = len(wrds_db)
WRDS_LIMITER_MIN = 5

# Error handlers:
if WRDS_LIMITER_MIN > wrds_limiter:
    wrds_limiter = WRDS_LIMITER_MIN
    print(f"\nDEBUG >> You're playing with the minimum words amount: {wrds_limiter}\n")
elif WRDS_LIMITER_MAX < wrds_limiter:
    wrds_limiter = WRDS_LIMITER_MAX
    print(f"\nDEBUG >> You're playing with all available words: {wrds_limiter}\n")

# Building temporary database:
wrds_selected = sample(wrds_db, wrds_limiter)
shuffle(wrds_selected)
print(wrds_selected)

# Building the app:
brain = GameBrain(wrds_selected)
ui = GameUI(brain, T_LIMITER)
