from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()            # ✨ Stops drawing lines
        self.hideturtle()       # ✨ Hides the turtle triangle
        self.goto(0, 200)  # ✨ Moves to a visible spot
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))

    def scores(self):
        self.score += 1
        self.update_scores()

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=('Arial', 16, 'normal'))

