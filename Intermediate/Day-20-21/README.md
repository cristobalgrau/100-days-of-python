# Day 20 and 21 - Build the Snake Game

# Project: The Snake Game

The Snake Game is a classic arcade-style game where the player controls a snake that moves around the screen, eating food to grow longer 
while avoiding collisions with itself and the walls. The objective is to grow the snake as long as possible without colliding, earning 
points for each piece of food eaten.

### Key Features:

- **Snake Movement:** The snake can move up, down, left, and right using arrow keys.
- **Food Generation:** Food appears randomly on the screen for the snake to eat. When the snake eats food, it grows longer.
- **Scoreboard:** A scoreboard displays the player's current score, updating each time the snake eats food.
- **Game Over Detection:** The game ends if the snake collides with itself or hits the wall. The final score is displayed, and the game restarts.

### Implementation:

- `main.py`: This file contains the main game loop where the snake, food, scoreboard, and game screen are initialized. It handles user input for controlling the snake and updates the game state accordingly.
- `snake.py`: This file defines the Snake class, which represents the snake object in the game. It includes methods for creating the snake, moving it, and changing its direction.
- `food.py`: This file defines the Food class, which represents the food object in the game. It randomly generates food on the screen for the snake to eat.
- `scoreboard.py`: This file defines the ScoreBoard class, which displays the player's score on the screen. It updates the score whenever the snake eats food and handles the game-over scenario.

  ### Result:

  ![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/45648cc3-57df-4a28-be5e-1f3eb02a1907)

  ![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/2f4e1e4d-272a-4a4d-bf2c-161e0b8dd978)

