from tkinter import *
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps

    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        timer_time = LONG_BREAK_MIN * 60
        timer_label.config(text="Break", fg=RED)
        window.deiconify()  # Restore the minimized windows
    elif reps % 2 == 0:
        timer_time = SHORT_BREAK_MIN * 60
        timer_label.config(text="Break", fg=PINK)
        window.deiconify()  # Restore the minimized windows
    else:
        timer_time = WORK_MIN * 60
        timer_label.config(text="Work", fg=GREEN)

    count_down(timer_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    count_min = count // 60
    count_sec = count % 60
    # formating counter as "00"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks ="✔️"
        if reps % 2 == 0:
            checkmark_label.config(text=checks * int(reps/2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark_label = Label(bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)


window.mainloop()
