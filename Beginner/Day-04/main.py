import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


rps_list = [rock, paper, scissors]

# index options: [A][B], where A is for computer_choice and B is for user_choice
# Using Rock=0, Paper=1 and Scissors=2
# rules [0][1] means the computer chose Rock and the user chose Paper, then the user "win" as the matrix value shows
rules = [["tied", "win", "lose"], ["lose", "tied", "win"], ["win", "lose", "tied"]]

user_choice = int(input ("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)

if not user_choice in range (0, 3):
    print ("You typed an invalid number, you lose!")
else:
    print (f"You chose:\n{rps_list[user_choice]}")
    print (f"Computer chose:\n{rps_list[computer_choice]}")
    print (f"***** You {rules [computer_choice][user_choice]} *****")
