"""

MORSE CODE TRANSLATOR HARD CODED BY @aldolammel
For translation double check, use this free online service: https://morsecode.world/international/translator.html

"""

# Initial values:
msg_translate = list()
# Constants:
MORSE = {
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
    ".": ".-.-.- ",
    ",": "--..-- ",
    "?": "..--.. ",
    "=": "-...- ",
    " ": "/"
}
# User message:
msg_user = input(str("Type a message to Titanic: ")).strip().upper()
# splitting the user message by letter:
msg_by_letter = [letter for letter in msg_user]
# Building the translation:
for letter in msg_by_letter:             # for each letter of the original msg...
    for key, value in MORSE.items():     # check each morse letter...
        if letter == key:                # if the checked morse letter's the same of the original msg letter...
            msg_translate.append(value)  # translate it, including to the translation list.
# Printing the translation out:
[print(letter, end="") for letter in msg_translate]
