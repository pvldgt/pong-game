from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.tracer(0)

# set up the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Old School Pong Game")

# create two paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

# listen for key presses that move the paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()