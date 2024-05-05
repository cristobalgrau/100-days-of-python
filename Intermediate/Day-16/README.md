# Day 16 - Object Oriented Programming (OOP)

## Project: Convert Day 15 Coffee Machine project into Object-Oriented Programming

This Coffee Machine Simulator program simulates the operation of a coffee machine using Object-Oriented Programming (OOP) principles.
The program consists of four main components:

- `main.py`: This file contains the main logic of the program. It initializes instances of the Menu, CoffeeMaker, and MoneyMachine classes and handles user interactions such as selecting drinks and generating reports.
- `menu.py`: This file defines the MenuItem and Menu classes. The MenuItem class represents each drink available in the menu, storing information such as name, ingredients, and cost. The Menu class manages the list of available drinks and provides methods to retrieve menu items and find drinks by name.
- `coffee_maker.py`: This file defines the CoffeeMaker class, which models the coffee-making functionality of the machine. It tracks the available resources (water, milk, coffee) and provides methods to check if there are sufficient resources to make a drink and to deduct the required resources when making a drink.
- `money_machine.py`: This file defines the MoneyMachine class, which handles the payment processing functionality of the machine. It tracks the machine's profit and the money received from the user. It provides methods to process coins inserted by the user, make payments for drinks, and calculate change.

