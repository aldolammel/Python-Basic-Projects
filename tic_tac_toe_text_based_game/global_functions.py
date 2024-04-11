def table_show(table):
    """
    Shows the Tic Tac Toe table.
    :param table: dictionary initially representing the empty spaces to be populated.
    :return: nothing.
    """
    print(f"{table['A1']} | {table['B1']} | {table['C1']}\n"
          f"{table['A2']} | {table['B2']} | {table['C2']}\n"
          f"{table['A3']} | {table['B3']} | {table['C3']}\n")


def table_edit(table, player, choice):
    """
    Provides the edition of one empty space on the table at the time, showing the updated table after all.
    :param table: dictionary initially representing the empty spaces to be populated.
    :param player: string with a character representing one of two available players.
    :param choice: string representing what position (e.g.: A3) must be edited.
    :return: call the function to show the updated table.
    """
    # Replace the empty space on table for the player character:
    table[choice] = player
    # Returning:
    return table_show(table)


def turn(table, empty, player, opts_col, opts_row):
    """
    Asks each player regarding their choices.
    :param table: dictionary initially representing the empty spaces to be populated.
    :param empty: which character represents the empty spaces on the game table.
    :param player: string with a character representing one of two available players.
    :param opts_col: string representing one of the three options corresponding the table columns.
    :param opts_row: string representing one of the three options corresponding the table rows.
    :return: string representing what position (e.g.: A3) must be edited.
    """
    # Looping to chose column letter:
    while True:
        # Take the user's choice for the column:
        col = input(f">> Player {player} | What column ({opts_col[0]}, {opts_col[1]}, {opts_col[2]}): ").strip().upper()
        # If the string is not composed by a letter, and if the col length is bigger than 1 char and not a valid option:
        if not col.isalpha() or len(col) > 1 or col not in opts_col:
            print("\nUse only available options for column. Try again!\n")
            continue
        break
    # Looping to chose row number:
    while True:
        # Take the user's choice for the row:
        row = input(f">> Player {player} | What row ({opts_row[0]}, {opts_row[1]}, {opts_row[2]}): ").strip()
        # If the string is not composed by number, and if the row length is bigger than 1 char and not a valid option:
        if not row.isnumeric() or len(row) > 1 or row not in opts_row:
            print("\nUse only available options for row. Try again!\n")
            continue
        break

    if table[col + row] != empty:
        print("\nThe spot chosen ISN'T available. Select another one!\n")
        return turn(table, empty, player, opts_col, opts_row)
    # Return the choices along as string, e.g. "B3":
    return col + row


def check_result(table, player):
    """
    Checks if the player has a full line of their character.
    :param table: dictionary initially representing the empty spaces to be populated.
    :param player: string with a character representing one of two available players.
    :return: bool. True if the selected player is the winner.
    """
    # Horizontal results:
    if table['A1'] == table['B1'] == table['C1']:
        if player == table['A1']:
            return True
    if table['A2'] == table['B2'] == table['C2']:
        if player == table['A2']:
            return True
    if table['A3'] == table['B3'] == table['C3']:
        if player == table['A3']:
            return True
    # Oblique results:
    if table['A1'] == table['B2'] == table['C3']:
        if player == table['A1']:
            return True
    if table['A3'] == table['B2'] == table['C1']:
        if player == table['A3']:
            return True
    # Vertical results:
    if table['A1'] == table['A2'] == table['A3']:
        if player == table['A1']:
            return True
    if table['B1'] == table['B2'] == table['B3']:
        if player == table['B1']:
            return True
    if table['C1'] == table['C2'] == table['C3']:
        if player == table['C1']:
            return True
    # if til this point the function doesn't return as True, it will return as False:
    return False
