from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(self.xcor(), 270)
        self.update_scoreboard()

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(self.high_score)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score {self.score}. High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
