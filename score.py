import os
HIGH_SCORE_FILE_PATH = os.path.join(os.path.dirname(__file__), "highscore.txt")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,320)
        self.score = 0
        self.highscore = self.get_highscore()
        self.color("LightCyan")
        self.display_score()

    def get_highscore(self):
        # Get highscore from file
        with open(HIGH_SCORE_FILE_PATH) as file:
            return int(file.read())

    def update_highscore(self):
        # Save new highscore
        with open(HIGH_SCORE_FILE_PATH,"w") as file:
            file.write(str(self.score))

    def display_score(self):
        # Display current and high score
        self.clear()
        self.write(f"Score: {self.score}         High score: {self.highscore}", align= "center",
                    font = ("Courier", 17, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0,0)
        # Update highscore if needed
        if self.score > self.highscore :
            self.update_highscore()
        self.write(f"-------- Game over --------\n\nFinal score: {self.score}\nHIGH SCORE: {self.get_highscore()}",
                    align= "center", font = ("Courier", 18, "bold"))
        
