from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.score = 0
        self.goto(0, 280)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align= "center", font= ('Arial', 12, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over_mssg(self):
        self.goto(0, 0)
        self.write("Game Over", align= "center")