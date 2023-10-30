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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5 * 60)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Study Timer")
# Adds padding to the window
window.config(padx=100, pady=50, bg=YELLOW)

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

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1, row=3)


reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=3, row=3)

check_marks = Label(text='✔', bg=YELLOW, fg=GREEN)
check_marks.grid(column=2,row=4)






window.mainloop()