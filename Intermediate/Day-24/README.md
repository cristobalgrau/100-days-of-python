# Day 24 - Files, Directories and Paths

This day we made 2 projects manipulating files and using Absolutes and Relative paths

## Project # 1: Add High Score feature to the Snake Game

For this project, we used the same code for the project Snake Game, made on days 20 and 21 and we add the feature to save the high score 
of the player in a file. To achieve this new feature we just create the method `reset_game()` in the class `ScoreBoard`

```python
def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
```

Where we evaluate if the current score is higher than the high_score saved.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/70da43f0-cecf-4a48-83a6-379a9a825f15)


## Project #2: Mail Merge

The Mail Merge script automates the process of generating personalized letters for a list of recipients, 
merging a template letter with individual names.

### Key Features:

- **Read Names from File:** The script reads a list of recipient names from the "invited_names.txt" file located in the `./Input/Names/` directory.
- **Read Template Letter:** It reads the content of the template letter from the "starting_letter.txt" file located in the `./Input/Letters/` directory.
- **Merge Names with Template:** For each recipient name, the script creates a personalized letter by replacing a placeholder (e.g., "[name]") in the template letter with the recipient's name.
- **Write Personalized Letters:** It writes the personalized letters to individual files in the `./Output/ReadyToSend/` directory, naming each file based on the recipient's name.

### Implementation:

- The script starts by reading the list of invited names from the "invited_names.txt" file and stripping any leading or trailing whitespace from each name.
- Next, it reads the content of the template letter from the "starting_letter.txt" file.
- For each recipient's name, the script replaces the placeholder "[name]" in the template letter with the recipient's name.
- It then creates a new text file for each personalized letter in the "./Output/ReadyToSend/" directory, naming each file based on the recipient's name.
- Finally, it writes the personalized letter content to each file.

### Result:

![image](https://github.com/cristobalgrau/100-days-of-python/assets/119089907/71fde286-db28-41d8-97b6-fdf825af8a74)
