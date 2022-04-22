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

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)

    ball.move()

    # detect collision of the ball with the top or bottom of the screen
    # and make the ball bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    # detect collision with paddles
    if (r_paddle.distance(ball) < 50 and ball.xcor() > 320) or (l_paddle.distance(ball) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detect if the ball goes past the paddles, if so, move back center and go to the opposite player




screen.exitonclick()