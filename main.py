from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.tracer(0)

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Old School Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# start listening for key presses that move the paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()