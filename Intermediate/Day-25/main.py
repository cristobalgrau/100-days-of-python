import turtle
import pandas as pd

FONT = ("Arial", 8, "normal")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pointer = turtle.Turtle()
pointer.hideturtle()

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_list = []
while len(answer_list) < 50:
    total = len(answer_list)
    answer_state = screen.textinput(title=f"Guess the State {total}/50", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in answer_list]
        ## List comprehension expanded
        # missing_states = []
        # for state in all_states:
        #     if state not in answer_list:
        #         missing_states.append(state)
        print(f"Missing {len(missing_states)} states")
        new_csv = pd.DataFrame(missing_states)
        new_csv.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        answer_list.append(answer_state)
        answer = data[data.state == answer_state]
        pointer.teleport(answer.x.iloc[0], answer.y.iloc[0])
        pointer.write(arg=answer_state, align="center", font=FONT)



# #********* Code to show the coordinates in the map when you click on it *********
# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
