from turtle import Turtle


class ScoreBoard(Turtle):
    score = 0
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setposition(0, 200)
        self.color("white")
        self.update_text()
    
    def increment_score(self):
        self.score += 1
        self.update_text()
    
    def update_text(self):
        self.clear()
        self.write(f"Score = {self.score}", move=False, align="center", font=("Arial", 8, "normal"))