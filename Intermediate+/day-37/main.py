import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from tkinter import *
from tkinter import messagebox
import webbrowser


# Pixela documentation: https://docs.pixe.la/

# Load environment variables from .env file
load_dotenv()

TOKEN = os.environ.get("PIXELA_TOKEN")
USERNAME = os.environ.get("PIXELA_USERNAME")
GRAPH_ID = "graph1"
headers = {"X-USER-TOKEN": TOKEN}

# ---- ENDPOINTS ----
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"


def create_pixela_user():
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_pixela_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "min",
        "type": "int",
        "color": "sora"
    }

    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def create_pixel():
    date = convert_date()
    qty = qty_entry.get()

    pixel_params = {
        "date": date,
        "quantity": qty
    }

    response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
    if response.status_code == 200:
        messagebox.showinfo(title="Created", message="Pixel created successfully.")
    else:
        messagebox.showerror(title="Error", message="Something went wrong!. Try again.")


def update_pixel():
    date = convert_date()
    qty = qty_entry.get()
    pixel_update_endpoint = f"{pixel_endpoint}/{date}"

    pixel_update_params = {
        "quantity": qty
    }

    response = requests.put(url=pixel_update_endpoint, json=pixel_update_params, headers=headers)
    if response.status_code == 200:
        messagebox.showinfo(title="Update", message="Pixel updated successfully.")
    else:
        messagebox.showerror(title="Error", message="Something went wrong!. Try again.")


def delete_pixel():
    date = convert_date()
    pixel_delete_endpoint = f"{pixel_endpoint}/{date}"

    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    if response.status_code == 200:
        messagebox.showinfo(title="Delete", message="Pixel deleted successfully.")
    else:
        messagebox.showerror(title="Error", message="Something went wrong!. Try again.")


def open_tracker_url():
    webbrowser.open(f"{pixel_endpoint}.html")


def convert_date():
    date = date_entry.get()
    new_date = datetime.strptime(date, '%m/%d/%Y')

    return new_date.strftime("%Y%m%d")


# ==================== MAIN ====================

# # Pixela User and Graph creation - Uncomment it for a project initialization
# create_pixela_user()
# create_pixela_graph()


# --------- GUI ---------

window = Tk()
window.title("Habit Tracker")
window.config(padx=40, pady=40)

canvas = Canvas(width=180, height=120)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(90, 0, anchor="n", image=logo_img)
canvas.grid(row=0, column=1, pady=(0, 40))

# Labels
date_label = Label(text="Study date: ")
date_label.grid(row=1, column=0)

qty_label = Label(text="Total minutes: ")
qty_label.grid(row=2, column=0)

# Entries
date_entry = Entry(width=30)
date_entry.grid(row=1, column=1, columnspan=2)
date_entry.insert(0, str(datetime.today().strftime("%m/%d/%Y")))
date_entry.focus()

qty_entry = Entry(width=30)
qty_entry.grid(row=2, column=1, columnspan=2)

# Buttons
create_button = Button(text="Create Pixel", command=create_pixel)
create_button.grid(row=3, column=0, pady=10)

update_button = Button(text="Update Pixel", command=update_pixel)
update_button.grid(row=3, column=1, pady=10)

delete_button = Button(text="Delete Pixel", command=delete_pixel)
delete_button.grid(row=3, column=2, pady=10)

tracker_button = Button(text="Visit Habit Tracker Webpage", command=open_tracker_url)
tracker_button.grid(row=4, column=0, columnspan=3)


window.mainloop()
