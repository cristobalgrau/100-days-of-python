from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")
random_card = {}


# ---------------------------- FLASHCARD MANAGEMENT ------------------------------- #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
finally:
    data_dict = pandas.DataFrame.to_dict(data, orient="records")


def random_flashcard():
    global random_card, flip_timer
    random_card = random.choice(data_dict)
    flip_timer = window.after_cancel(flip_timer)
    canvas.itemconfig(flashcard, image=front_card_img)
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=random_card["French"], fill="black")
    flip_timer = window.after(3000, flip_flashcard)


def flip_flashcard():
    canvas.itemconfig(flashcard, image=back_card_img)
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=random_card["English"], fill="white")


def remove_word():
    data_dict.remove(random_card)
    new_data = pandas.DataFrame(data_dict)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    random_flashcard()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, width=800, height=800, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_flashcard)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="./images/card_front.png")
back_card_img = PhotoImage(file="./images/card_back.png")
flashcard = canvas.create_image(400, 260, image=front_card_img)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
language_label = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT)
word_label = canvas.create_text(400, 263, text="", font=WORD_FONT)

# Buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_flashcard)
wrong_button.grid(row=1, column=0)

random_flashcard()


window.mainloop()
