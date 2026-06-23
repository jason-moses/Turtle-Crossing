from turtle import Turtle, Screen
import random

screen = Screen()
CARS = ["YellowCar.gif", "RedCar.gif", "GreenCar.gif", "BlueCar.gif"]
screen.register_shape(CARS[0])
screen.register_shape(CARS[1])
screen.register_shape(CARS[2])
screen.register_shape(CARS[3])
STARTING_DISTANCE_NORMAL = 5
STARTING_DISTANCE_HARD = 10
MOVE_INCREMENT = 3

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.play_type = screen.textinput("Choose your difficulty:\n (Normal/Hard)", "")
        if self.play_type == "Normal" or "normal":
            self.car_speed = STARTING_DISTANCE_NORMAL

        elif self.play_type == "Hard" or "hard":
            self.car_speed = STARTING_DISTANCE_HARD

        else:
            self.car_speed = STARTING_DISTANCE_NORMAL

    def create_cars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.shape(CARS[random.randint(0,3)])
            new_car.penup()
            # Switching to semi-random instead of perfectly random y_pos()
            # Semi-random y_pos() avoids vehicle overlap
            random_y = random.randint(-10, 10) * 25
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

