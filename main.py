import time
import winsound

from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)

game_on = True

screen.listen()
screen.onkey(player.go_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    #Detect death
    for car in car_manager.all_cars:
        if player.distance(car) < 23:
            game_on = False
            scoreboard.write_game_over()
            winsound.PlaySound("Womp-Womp-Womp.wav", winsound.SND_ASYNC)

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.increase_speed()
        scoreboard.write_level()
        winsound.PlaySound("Level-Up.wav", winsound.SND_ASYNC)




screen.exitonclick()