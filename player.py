from turtle import Turtle


MOVE_DISTANCE = 20

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -275)

    def move_up(self):
        self.forward(MOVE_DISTANCE)