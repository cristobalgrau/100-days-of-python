from tkinter import *


def convert_miles():
    km = round(float(miles_input.get()) * 1.609344, 2)
    label_result.config(text=km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=40)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label: Miles
label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

# Label: is equal to
label_equal_to = Label(text="is equal to")
label_equal_to.grid(column=0, row=1)

# Label: Result
label_result = Label(text=0)
label_result.grid(column=1, row=1)

# Label: Km
label_km = Label(text="Km")
label_km.grid(column=2, row=1)

# Button: Calculate
button = Button(text="Calculate", command=convert_miles)
button.grid(column=1, row=2)


window.mainloop()
