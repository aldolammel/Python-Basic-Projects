import functions
import pandas

# Opening database:
states_original = pandas.read_csv("50_states.csv")
states = states_original.to_dict()
SCORE_LIMIT = len(states["state"])

# Initial values:
player_hits = list()
current_score = 0

# Starting the game:
is_gaming = True
while is_gaming:

    answer = functions.question(current_score, SCORE_LIMIT)
    score = functions.check_answer(answer, current_score, states, player_hits)
    current_score = score
    is_gaming = functions.check_end(answer, states)
