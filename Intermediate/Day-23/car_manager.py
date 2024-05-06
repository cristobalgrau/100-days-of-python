from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# To avoid car position overlapping
y_pos = []
for i in range(-250, 250, 20):
    y_pos.append(i)


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            y_position = random.choice(y_pos)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.current_speed)

    def update_car_speed(self):
        self.current_speed += MOVE_INCREMENT
