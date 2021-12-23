import time
from turtle import Screen

import car_manager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("LightBlue")
screen.tracer(0)

scoreboard = Scoreboard()

screen.listen()
player = Player()
car_manager = car_manager.CarManager()

screen.onkey(player.move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.level += 1
        scoreboard.update_scoreboard()


screen.exitonclick()
