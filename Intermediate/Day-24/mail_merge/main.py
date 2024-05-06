with open("./Input/Names/invited_names.txt")as file:
    invited_names = file.readlines()
    for index in range(len(invited_names)):
        invited_names[index] = invited_names[index].strip()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_lines = file.readlines()

replace_word = "[name]"
for name in invited_names:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        letter_lines[0] = letter_lines[0].replace(replace_word, name)
        for line in letter_lines:
            file.write(line)
        replace_word = name
