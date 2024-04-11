import global_functions as fnc

# INITIAL VALUES:
is_new_game = True
is_running = True
is_winner = False
table = dict()

# CONSTANTS:
PLAYER_X = "X"
PLAYER_O = "O"
OPTS_COL = ["A", "B", "C"]
OPTS_ROW = ["1", "2", "3"]
EMPTY = "."

print("TIC TAC TOE text-based game by @aldolammel\n")

while is_new_game:
    # DECLARATIONS:
    table = {
        "A1": EMPTY,
        "B1": EMPTY,
        "C1": EMPTY,
        "A2": EMPTY,
        "B2": EMPTY,
        "C2": EMPTY,
        "A3": EMPTY,
        "B3": EMPTY,
        "C3": EMPTY
    }
    # Game starts:
    fnc.table_show(table)
    # Game loop starts:
    while is_running:
        # Turn of player X:
        choice = fnc.turn(table, EMPTY, PLAYER_X, OPTS_COL, OPTS_ROW)
        fnc.table_edit(table, PLAYER_X, choice)
        # Checking choice:
        is_winner = fnc.check_result(table, PLAYER_X)
        if is_winner:
            print(f"\nPlayer {PLAYER_X} wins!\n")
            break
        # Turn of player O:
        choice = fnc.turn(table, EMPTY, PLAYER_O, OPTS_COL, OPTS_ROW)
        fnc.table_edit(table, PLAYER_O, choice)
        # Checking choice:
        is_winner = fnc.check_result(table, PLAYER_O)
        if is_winner:
            print(f"\nPlayer {PLAYER_O} wins!\n")
            break
        # Checks the table available values:
        is_running = False
        for value in table.values():
            # If there's at least one empty value:
            if value == EMPTY:
                is_running = True
                # break the looping, keeping the game running:
                break
    # The game must be stopped:
    if not is_running:
        print("\nThe match draw!\n")

    choice = input("Wanna play again? (Yes = press any / Exit = N): ").strip().upper()
    if choice == "N":
        print("\nThe game has been finished.")
        break
