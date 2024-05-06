# Day 23 - The Turtle Crossing Capstone Project

## Project: Turtle Crossing Game

The Turtle Crossing Game is a classic arcade-style game where players control a turtle trying to cross a busy highway. 
As the player navigates their way across the road, they must avoid oncoming traffic to reach safety on the other side. 
With each successful crossing, the game starts to increase the speed of the cars.

### Key Features:

- **Crossing Traffic:** The game simulates traffic using car objects created by the CarManager class. Cars move horizontally across the screen at varying speeds, posing obstacles for the player's turtle to navigate around.
- **Increasing Difficulty:** With each successful crossing, the speed of the traffic increases. This feature is implemented in the CarManager class, where the update_car_speed method gradually increments the speed of the cars.
- **Score Tracking:** The Scoreboard class keeps track of the player's score and displays it on the screen. The score increases with each successful crossing, and the level is updated accordingly.
- **Collision Detection:** Collision detection is implemented between the player's turtle and the oncoming cars. If a collision occurs, the game ends, and the "GAME OVER" message is displayed. This functionality is managed in the Main.py file, where the game loop checks for collisions between the player and cars.
- **User Interaction:** Players control the turtle's movement using arrow keys. The Player class defines the turtle's movement behavior, allowing it to move vertically on the screen to avoid collisions with cars.

## Modules and Classes:

- `main.py`: Manages the game loop, initializes game objects (player, cars, scoreboard), and handles user input.
- `player.py`: Defines the player's turtle, including its appearance, movement behavior, and starting position.
- `car_manager.py`: Controls the behavior of the cars, including their movement across the screen, creation at random intervals, and increasing speed with each level.
- `scoreboard.py`: Manages the game's score and level display, updating them as the player progresses through the game and displaying the "GAME OVER" message when necessary.

### Result

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/71496065-b4da-4561-838a-48def524ca5f)

