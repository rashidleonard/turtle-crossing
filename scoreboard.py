from turtle import Turtle

FONT = ("Courier", 24, "normal")

DISPLAY = (-200, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(DISPLAY)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def new_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)

