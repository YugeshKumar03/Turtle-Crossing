from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 10

class Car(Turtle):
    def __init__(self, speed_val):
        super().__init__()
        self.shape("square")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid= 1, stretch_len= 2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.speedval = speed_val
        self.move_forward()

    def move_forward(self):
        if self.xcor() > -300:
            self.forward(MOVE_DISTANCE * (1 + self.speedval/4))
            #self.move_forward()

class CarManager:
    def __init__(self, level):
        self.level = level
        self.objects = []
        self.spawn_cars()

    def spawn_cars(self):
        car = Car(self.level)
        car.goto(280, random.randrange(-240, 240, 25))
        self.objects.append(car)

    def end_round(self):
        for car in self.objects:
            car.ht()
            del car
        self.objects = []

    def clear_end_car(self):
        for car in self.objects:
            if car.xcor() < -300:
                car.ht()
                del car

