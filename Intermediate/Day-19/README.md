# Day 19 - Instances, State and Higher Order Functions

This day we made 2 project using the `turtle` library

## Project #1: Etch-A-Sketch

The "Etch-A-Sketch" project simulates the functionality of a classic Etch-A-Sketch toy using the Python turtle module. 
Users can control a turtle graphic on the screen to draw lines and shapes in a similar manner to the physical toy.

### Key Features:

1. **Drawing Controls:**
- Users can control the movement of the turtle using the keyboard keys. The arrow keys "w", "s", "a", and "d" are used to move the turtle forwards, backwards, left, and right, respectively.
- These controls allow users to navigate the turtle across the screen and create drawings by leaving a trail behind as it moves.

2. **Clearing the Drawing:**
- To reset the drawing canvas, users can press the "c" key. This action clears the screen, removing all drawn lines and shapes.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/50b4753e-d860-4e2b-aab5-ef8ea9173ad8)



## Project #2: Turtle Race

The "Turtle Race" project simulates a race between turtles of different colors using the Python `turtle` library. 
Users can participate by betting on the winning turtle's color before the race begins.

### Key Features:

1. **User Bet:**
- Before the race starts, users are prompted to make a bet by selecting a turtle color from a list of available options.
- Users input their choice through a text input dialog box, specifying the color of the turtle they believe will win the race.

2. **Race Initialization:**
- Turtles of various colors are created and positioned at the starting line on the left side of the screen.
- Each turtle is assigned a unique color and placed evenly spaced along the y-axis to represent the racing lanes.

3. **Race Execution:**
- Once the user has made their bet, the race begins. Turtles move forward randomly with each iteration of the race loop.
- The race continues until one of the turtles crosses the finish line on the right side of the screen.

4. **Determining the Winner:**
- When a turtle reaches the finish line, the race ends, and the winning turtle's color is determined.
- If the user's bet matches the winning turtle's color, a message indicating victory is displayed. Otherwise, a message of defeat is shown.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/deb17859-46a1-44e1-a6b9-802e4041afbe)

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/25f7dcf6-99dc-4e3f-8944-78407a360f91)
