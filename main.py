from turtle import Turtle, Screen
import time
from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager, Car

screen = Screen()
screen.screensize(canvwidth= 600, canvheight= 600)
screen.tracer(0)

player_turtle = Player()
score = ScoreBoard()

screen.listen()
screen.onkeypress(player_turtle.move_up, "Up")

game_is_on = True
level = 1
car_spawner = CarManager(level)
time_val = 0

while game_is_on:
    screen.update()
    time.sleep(0.1)
    if time_val%4 == 0:
        car_spawner.spawn_cars()
    for car in car_spawner.objects:
        car.move_forward()
    car_spawner.clear_end_car()

    if player_turtle.ycor() > 270:
        score.update_score()
        level += 1
        car_spawner.end_round()
        time.sleep(2)
        player_turtle.goto(0, -275)
        car_spawner = CarManager(level)
    time_val += 1
    for car in car_spawner.objects:
        if car.distance(player_turtle) < 22:
            game_is_on = False
            score.game_over_mssg()

screen.exitonclick()