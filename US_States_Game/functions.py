from turtle import Screen, Turtle
from state_title import StatesTitle
from time import sleep

# Creating the interface:
image_bg = "blank_states_img.gif"
screen = Screen()
screen.title("U.S. States Game by @aldolammel")
screen.setup(width=800, height=600)
screen.addshape(image_bg)
bg = Turtle()
bg.shape(image_bg)

# MY COLORS
corT = '\033[1;32m'
corF = '\033[1;31m'
corOut = '\033[m'


def question(score, limit):
    last_score = limit - 1
    print("Type 'exit' to give up and check the states you've missed.\n")

    txt_ask = "What's another state name?"
    if score == 0:
        txt_ask = "What's a state name?"
    if score == last_score:
        txt_ask = "Now the last state!"

    answer = screen.textinput(title=f"{score}/{limit} states discovered", prompt=txt_ask).strip().title()

    return answer


def check_answer(answer, score, states, player_hits):
    if answer in player_hits:
        print(f"You had already discovered {answer} state.", end=" ")
        return score

    for key, value in states["state"].items():
        if value == answer:
            player_hits.append(answer)

            coord_x = states["x"][key]
            coord_y = states["y"][key]
            position = [coord_x, coord_y]
            StatesTitle(answer, position)

            del states["state"][key]
            del states["x"][key]
            del states["y"][key]

            if len(states["state"]) > 0:
                print(f"{corT}{answer}{corOut} is right! You got other {len(states['state'])} states to figure out!",
                      end=" ")

            new_score = score + 1
            return new_score

    if answer != "Exit":
        print(f"There is no US state called {corF}{answer}{corOut}.", end=" ")

    return score


def check_end(answer, states):
    if answer == "Exit":
        print(f"{corF}You missed {len(states['state'])} states:{corOut} {states['state']}", end=" ")
        return False

    if len(states["state"]) == 0:
        sleep(0.5)
        print(f"Your last was {corT}{answer}{corOut}!\n{corT}You win! Congrats!{corOut}{corOut}")
        sleep(3)
        return False

    return True
