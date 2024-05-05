import random
import turtle as t


marker = t.Turtle()
t.colormode(255)
color_list = [(249, 228, 17), (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20), (33, 90, 188), (43, 212, 71)]
marker.speed("fastest")
marker.penup()
marker.hideturtle()

for line in range(-200, 300, 50):
    marker.teleport(-300, line)
    for _ in range(10):
        marker.dot(20, random.choice(color_list))
        marker.forward(50)


screen = t.Screen()
screen.exitonclick()
