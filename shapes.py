from turtle import Turtle
import random

class Shape(Turtle):
    def __init__ (self):
        super().__init__()
        self.penup()
        self.colors = ("red","LightSlateGray","GreenYellow","DarkOrange","Orchid","MediumPurple","MediumVioletRed","LimeGreen")
        self.shapes = ("triangle", "turtle", "circle","square","square")
        self.random_shape()
    

    def random_shape(self):
        self.clear()

        # Random start x position from top
        self.random_x = random.randint(-370,370)
        self.goto(self.random_x, 370)

        # Random shape size
        self.random_size = random.uniform(0.5,2)
        self.shapesize(self.random_size,self.random_size)

        # 1 in 5 chance of being a dangerous white shape
        if random.randint(1,5) == 1:
            self.color("white")
        else:
            self.color(random.choice(self.colors))

        # Random shape
        self.shape(random.choice(self.shapes))
        self.setheading(270)  # Falling direction