from turtle import Turtle

FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.write_level()

    def write_level(self):
        self.clear()
        self.level_up()
        self.goto(-280,260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def level_up(self):
        self.level += 1

    def write_game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align="center", font=FONT)

