from tkinter import Tk, Label, Button, Canvas, PhotoImage
from math import floor
from playsound import playsound

# ---------------------------- CONSTANTS & INITIAL DECLARATIONS --------------------------------------------------------
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25  # original is 25
SHORT_BREAK_MIN = 5  # original is 5
LONG_BREAK_MIN = 20  # original is 20
TXT_BUTTONS = ("Arial", 12, "normal")
CLOCK_ZEROED = "00:00"
TITLE_WAIT = ""
TITLE_WORK = "Working"
TITLE_SHORT_BREAK = "Resting"
TITLE_LONG_BREAK = "Take a break"
CHECK_MARK_CYCLE = "✓"
BT_START = "Start to work"
BT_RESET = "Reset"
ONE_SEC = 1000  # 1 second has 1000 mileseconds
WINDOW_WIDTH = 380  # pixels
WINDOW_HEIGHT = 400  # pixels
WINDOW_PADDING = 50  # pixels

timer = str()
reps = 0
work_reps = 0
is_work_running = False

# ---------------------------- TIMER RESET -----------------------------------------------------------------------------


def reset():
    global timer
    global reps
    global work_reps

    # Canceling the counting:
    window.after_cancel(timer)

    # Checking the buttons:
    bt_start.config(text=BT_START, command=start_timer)
    bt_reset.config(text="", command=do_nothing)

    # Reseting
    reps = 0
    work_reps = 0
    lb_title.config(text=TITLE_WAIT, fg=RED)
    canvas.itemconfig(txt_timer, text=CLOCK_ZEROED)
    lb_check_mark.config(text="")


# ---------------------------- TIMER MECHANISM -------------------------------------------------------------------------


def do_nothing():
    print("This button is temporally disabled.")


def start_timer():
    global reps
    global work_reps
    global is_work_running
    reps += 1

    # Checking the buttons:
    bt_start.config(text="", command=do_nothing)
    bt_reset.config(text=BT_RESET, command=reset)

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 1st, 3rd, 5th or 7th rep:
    if reps in [1, 3, 5, 7]:
        is_work_running = True
        playsound('./sounds/work.wav')

        lb_title.config(text=TITLE_WORK, fg=RED)
        count_down(work_sec)

    else:
        is_work_running = False

        # If the 2nd, 4th or 6th rep:
        if reps in [2, 4, 6]:
            lb_title.config(text=TITLE_SHORT_BREAK, fg=GREEN)
            playsound('./sounds/rest.wav')
            count_down(short_break_sec)

        # If it's the 8th rep:
        else:
            lb_title.config(text=TITLE_LONG_BREAK, fg=GREEN)
            playsound('./sounds/long_rest.wav')
            count_down(long_break_sec)


# ---------------------------- COUNT DOWN MECHANISM --------------------------------------------------------------------


def count_down(count):
    global reps
    global work_reps
    global timer

    count_min = floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(txt_timer, text=f"{count_min:02d}:{count_sec:02d}")

    if count > 0:
        timer = window.after(ONE_SEC, count_down, count - 1)
    else:
        if is_work_running:
            work_reps += 1
            lb_check_mark.config(text=f"{CHECK_MARK_CYCLE * work_reps}")
        if reps < 8:
            start_timer()
        else:
            playsound("./sounds/cycle_finished.wav")
            reset()


# ---------------------------- UI SETUP --------------------------------------------------------------------------------


window = Tk()
window.minsize(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.config(padx=WINDOW_PADDING, pady=WINDOW_PADDING, bg=YELLOW)
window.title("Pomodoro by @aldolammel")

bg_img = PhotoImage(file="tomato.png")
canvas_max_width = WINDOW_WIDTH - (WINDOW_PADDING * 2)
canvas = Canvas(width=canvas_max_width, height=226, bg=YELLOW, highlightthickness=0)
canvas.create_image(140, 114, image=bg_img)
txt_timer = canvas.create_text(140, 134, text=CLOCK_ZEROED, font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=0, row=1)

# Labels
lb_title = Label(text=TITLE_WAIT, font=(FONT_NAME, 24, "bold"), fg=RED, bg=YELLOW, highlightthickness=0)
lb_title.grid(column=0, row=0)
lb_check_mark = Label(text="", font=(FONT_NAME, 18), fg=GREEN, bg=YELLOW, highlightthickness=0)
lb_check_mark.grid(column=0, row=2)

# Buttons
bt_start = Button(text=BT_START, command=start_timer)
bt_start.grid(column=0, row=3)
bt_reset = Button(text="", command=do_nothing)
bt_reset.grid(column=0, row=4)

window.mainloop()  # keep the Tkinter window on screen
