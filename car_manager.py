from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


# STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            y_axis = random.randint(-200, 200)
            car.goto(300, y_axis)
            # car.setheading(270)
            self.all_cars.append(car)

    def move(self):
        for a_car in self.all_cars:
            a_car.setheading(180)
            a_car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += STARTING_MOVE_DISTANCE
