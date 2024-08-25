# Day 48: Selenium Webdriver Browser and Game-Playing Bot

## Project: Create an Automated Game Playing Bot

This project automates gameplay for the popular browser game "Cookie Clicker" using Python and Selenium. The bot continuously clicks the cookie on the screen, simulating user interaction to generate cookies. Additionally, it monitors the in-game store and automatically purchases the most expensive item affordable with the current amount of cookies.

### Key Features:

- Automates clicking the cookie in "Cookie Clicker" to generate cookies passively.
- Monitors the in-game store prices.
- Analyzes available cookies and automatically purchases the most expensive item within budget.
- Provides information on the cookies per second (CPS) after a set runtime.

### Libraries Used:

- `selenium`: This library allows for automating web browser interactions. It enables the script to find elements on the screen (like the cookie) and click on them.
- `datetime`: This library helps the script track the running time and control the automation duration.

### Implementation:

The script follows these main steps:

1. **Initializes the Chrome browser**: It sets up a headless Chrome browser instance to run the automation in the background.

2. **Navigates to the game**: The script opens the "Cookie Clicker" website using the provided URL.

3. **Locates elements on the screen**: It identifies the cookie element and the list of items in the store using their unique IDs and CSS selectors.

4. **Auto-clicks the cookie**: The script enters a loop that continuously clicks the cookie at a set interval (5 seconds).

5. **Tracks generated cookies**: It monitors the in-game currency ("money") displayed on the screen and updates the value after each click cycle.

6. **Analyzes store prices**: A function called `get_menu_prices` retrieves the prices of all available items in the store and creates a dictionary for easy access.
    ```python
    def get_menu_prices():
        menu_prices = {}
        for x in store:
          if x.text != "":
            price = int(x.text.strip().split("-")[1].replace(",", ""))
            menu_prices[x.text.split("-")[0].strip()] = price
        return menu_prices
    ```
    This function iterates through each item in the store list (store) and extracts the price information. It removes unnecessary characters, converts the price to an integer, and stores it in a dictionary with the item name as the key.

8. **Purchases the most expensive item**: The function `get_most_expensive_item` analyzes the available money and the store prices. It then identifies and purchases the most expensive item the user can afford.
    ```python
    def get_most_expensive_item(available_money):
        higher_price = 0
        affordable_item_name = ""
        for n in store:
          if n.text != "":
            item_price = int(n.text.strip().split("-")[1].replace(",", ""))
            if available_money > item_price > higher_price:
              higher_price = item_price
              affordable_item_name = n.text.split("-")[0].strip()
        return affordable_item_name
    ```
    
9. **Tracks running time**: The script runs for a predetermined duration (1 minute) defined at the beginning.

10. **Reports results**: After the runtime is completed, the script retrieves and displays the current "cookies per second" (CPS) value.

### Learning Objectives:

This project provides hands-on experience with the following concepts:

- Web automation using Selenium
- Extracting data from a website
- Working with web elements and attributes
- Automating repetitive tasks
- Integrating external libraries in Python


## Result:

![image](https://github.com/user-attachments/assets/16da8a17-3a90-41cd-a46b-ba47b8ac871b)

![image](https://github.com/user-attachments/assets/9118f035-a70c-4bdf-b290-b21aee0d67c7)


