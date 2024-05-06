# Day 22 - Build Pong: The Famous Arcade Game

## Project: Pong Game

The project simulates the classic arcade game Pong, where players control paddles to hit a ball back and forth across the screen. 
This Python implementation utilizes the Turtle module for graphics and user input handling.

### Key Features:

- **Gameplay:** Players control paddles with keyboard inputs ('Up' and 'Down' arrows for the right paddle, 'W' and 'S' keys for the left paddle) to hit the ball and prevent it from passing their side of the screen.
- **Scoring:** The ScoreBoard class keeps track of the scores for both players, updating them whenever a player misses the ball.
- **Ball Movement:** The Ball class governs the movement of the ball, including bouncing off walls and paddles. The ball's speed increases with each bounce off the paddles, creating progressively challenging gameplay.
- **Game Over:** The game ends when one player misses the ball. The ScoreBoard displays the final scores, and players can exit the game by closing the window.

### Modules and Classes:

- `main.py`: Initializes the game window and controls the main game loop.
- `paddle.py`: Defines the Paddle class, which represents the paddles controlled by the players.
- `ball.py`: Contains the Ball class, responsible for managing the ball's behavior.
- `scoreboard.py`: Implements the ScoreBoard class to display and update the scores during gameplay.

### Result

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/2473426c-5434-46f1-8375-10fb6d7cfaa8)
