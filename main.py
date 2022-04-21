from turtle import Screen
from paddle import Paddle

import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Old School Pong Game")

paddle = Paddle()

# start listening for key presses that set the snake heading
screen.listen()
screen.onkey(paddle.right_up, "Up")
screen.onkey(paddle.right_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    paddle.move(paddle.right_paddle)

    # detect collision with upper and lower bounds
    if paddle.right_paddle.ycor() > 290:
        paddle.right_down()
    elif paddle.right_paddle.ycor() < -290:
        paddle.right_up()






screen.exitonclick()