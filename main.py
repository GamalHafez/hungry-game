from turtle import Screen
from paddle import Paddle
from shapes import Shape
from score import Scoreboard
import time
import random

# Setup screen
screen = Screen()
screen.setup(width = 800, height = 800)
screen.bgcolor("black")
screen.title("Hungry game")
screen.tracer(0)

# Initialize game components
paddle  = Paddle()
shape = Shape()
score = Scoreboard()

# Listen to user input
screen.listen()
screen.onkey(paddle.move_right,"Right")
screen.onkey(paddle.move_left,"Left")


# Game state

default_forward = 10
all_shapes = []
all_shapes.append(shape)

game_on = True
while game_on:
    screen.update()
    score.display_score()

    # Move shapes
    if len(all_shapes) == 1:
        shape.forward(default_forward)
    else:
        speeds = (10,17,25,20,19,21,19,20,20,21)
        for x in all_shapes:
            x.forward(speeds[all_shapes.index(x)])

    for x in all_shapes:
        # Shape reaches paddle level
        if x.ycor() <= -330 and x.distance(paddle) < 70:
            if x.color()[0] == "white":
                 # White = instant game over
                score.game_over()
                game_on = False

            elif x.shape() == "square":
                score.score += 2
            elif x.shape() == "triangle":
                score.score = 0 # triangle resets score
            elif x.shape() == "turtle":
                score.score += 3
            else:
                score.score += 1

            # Reset shape
            x.random_shape()

            if default_forward < 25:
                default_forward += 2

        # Shape falls off screen without catching
        if x.ycor() <= -400:
            x.random_shape()


    

    # Add more shapes as score increases
    if score.score >= 15 and len(all_shapes) <= 2:
        all_shapes.append(Shape())

    elif score.score >= 20 and len(all_shapes) <= 3:
        all_shapes.append(Shape())

    elif score.score >= 50 and len(all_shapes) <= 4:
        all_shapes.append(Shape())

    elif score.score >= 75 and len(all_shapes) <= 7:
        all_shapes.append(Shape())

    time.sleep(0.1)


screen.exitonclick()