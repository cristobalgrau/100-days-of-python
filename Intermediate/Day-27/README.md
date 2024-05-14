# Day 27 - Tkinter, *args, **kwargs and Creating GUI Programs

## Project: Miles to Kilometers Converter

The Miles to Kilometers Converter is a simple graphical application built using the Tkinter library in Python. 
It allows users to convert distances from miles to kilometers. By entering a distance in miles and clicking 
the "Calculate" button, users can instantly see the equivalent distance in kilometers displayed on the interface.

### Key Features:

- **Input and Output Fields:** The application provides a text entry field where users can input the distance in miles. Upon calculation, the converted distance in kilometers is displayed dynamically on the interface.
- **Conversion Logic:** The conversion formula used is 1 mile = 1.609344 kilometers. The application calculates the equivalent kilometers by multiplying the input miles by this conversion factor and rounds the result to two decimal places for accuracy.
- **User Interaction:** Users can interact with the application through a user-friendly graphical interface. The "Calculate" button triggers the conversion process, making it intuitive for users to perform conversions.

### Libraries, Classes, and Widgets:

- `tkinter`: Python's standard GUI (Graphical User Interface) toolkit used for creating graphical applications.
- `Tk()`: Represents the main window or root window of the application.
- `Entry()`: Widget for accepting single-line text input from the user.
- `Label()`: Widget used to display static text or images on the interface.
- `Button()`: Widget that triggers an action or function when clicked by the user.

### Implementation:

The application window is created using Tkinter's `Tk()` class. It includes an entry field for inputting miles, labels for indicating units, 
and a button to initiate the conversion process. When the user clicks the "Calculate" button, the `convert_miles` function is called, which 
retrieves the input miles, performs the conversion, and updates the result label with the equivalent distance in kilometers.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/3c3cb5bc-e86d-41a4-9508-33f1205ff37b)

