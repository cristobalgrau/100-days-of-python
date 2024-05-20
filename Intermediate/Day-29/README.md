# Day 29 - Building a Password Manager GUI App with Tkinter

## Project: Password Manager GUI App

The Password Manager GUI App is a robust application designed to help users generate and store complex passwords securely. 
The app offers a user-friendly graphical interface to save a password or generate a random one, copy them to the clipboard, and save them 
along with the associated website and username information in a local file.

### Key Features:

- **Password Generation:** Generates secure passwords containing letters, symbols, and numbers with customizable lengths.
- **Clipboard Copy:** Automatically copies the generated password to the clipboard for easy pasting.
- **Data Storage:** Saves the website, username, and password details to a local file in a structured format.
- **User Interaction:** Provides intuitive prompts and warnings to ensure that all fields are filled and details are correct before saving.

### Libraries, Classes, and Widgets:

- `Tkinter`: Used to create the graphical user interface (GUI) elements such as windows, buttons, labels, and entry fields.
- `random`: Utilized for generating random letters, numbers, and symbols for secure passwords.
- `pyperclip`: Allows the application to copy the generated password directly to the clipboard.
- `messagebox`: A submodule of Tkinter used for displaying warning and confirmation dialogs.

### Implementation:

The Password Manager GUI App is built using the Tkinter library for the graphical interface.

The generate_password function uses the random module to create a secure password by randomly selecting characters from predefined lists of letters, 
numbers, and symbols. The password is then shuffled to ensure randomness. The generated password is displayed in the password entry field using 
`password_entry.insert(0, password)` and copied to the clipboard using `pyperclip.copy(password)`.

The save function collects input from the user via the entry fields for website, email/username, and password. It first checks if any fields are empty 
and display a warning using `messagebox.showwarning` if necessary. Upon confirmation from the user through `messagebox.askokcancel`, the details are 
appended to data.txt in a formatted manner. This function ensures data persistence by opening the file in append mode ("a") and writing the input data.

The graphical interface is set up using `Tkinter`. The main window is created with `window = Tk()`, and its properties are configured with `window.config()`. 
The Canvas widget is used to display the app logo, and various Label widgets guide the user. Entry widgets allow the user to input website, email/username, 
and password information. The Button widgets trigger the password generation and data saving functions. Each widget is positioned using the `grid` method to 
organize them into a coherent layout.

The app runs within the `window.mainloop()`, which keeps the application window open and responsive to user interactions. This loop waits for events such as 
button clicks to trigger the corresponding functions, ensuring a dynamic and interactive user experience.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/97c56f5f-d56a-4438-8ff5-83e721e2f04c)


