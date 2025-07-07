from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(0.6 , 7) # Thin horizontal paddle
        self.goto(0,-320)

    def move_right(self):
        # Move right with screen boundary check
        if self.xcor() + 30 < 330:
            self.goto(self.xcor() + 30, self.ycor())
        else:
            target_x = 330 - self.xcor()
            self.goto(self.xcor() + target_x,  self.ycor())


    def move_left(self):
        # Move left with screen boundary check
        if self.xcor() -  30 > -330:
            self.goto(self.xcor() - 30, self.ycor())
        else:
            target_x = -330 -  self.xcor()
            self.goto(self.xcor() + target_x, self.ycor())