from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_ =  None

# ---------------------------- TIMER RESET ------------------------------- # 
# Resets the timer
def reset_timer():
    window.after_cancel(timer_)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps 
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    # Changes the Timer name and color 
    reps += 1 
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(work_sec)
        timer.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer_
        timer_ =  window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study Timer")
# Adds padding to the window
window.config(padx=100, pady=50, bg=YELLOW)

# Creates the Timer label 
timer = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
timer.grid(column=2, row=1)

# Changes the bg color and removes the border from the image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Making an image the back ground
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)

# Adds text OVER the background image
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=2,row=2)

# Creates a start button
start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)

# Creates a reset button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)

# Creates a check mark 
check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=2,row=4)






window.mainloop()