from db import db_en

from game_brain import GameBrain
from game_ui import GameUI

# Game Setup:
wrds_db = list(db_en)
wrds_limiter = 40  # Number of words.
t_limiter = 120  # Timeout for run in seconds.

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

T_LIMITER_MIN = wrds_limiter * 0.5
if T_LIMITER_MIN > t_limiter:
    t_limiter = T_LIMITER_MIN
    print(f"\nDEBUG >> Your timeout's too low, so it was reset to the minimum duration based on words number: "
          f"{t_limiter} secs.\n")

# Building the app:
brain = GameBrain(wrds_db, wrds_limiter)
GameUI(brain, t_limiter)
