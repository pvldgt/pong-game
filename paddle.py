from turtle import Turtle

UP = 90
DOWN = 270
R_P_X = 350
L_P_X = -350
Y = 0
POSITIONS = [(R_P_X, Y), (L_P_X, Y)]

class Paddle():

    def __init__(self):
        self.paddle_list = []
        self.create_paddles()
        self.right_paddle = self.paddle_list[0]
        self.left_paddle = self.paddle_list[1]

    def create_paddles(self):
        for position in POSITIONS:
            self.add_paddle(position)

    def add_paddle(self, position):
        paddle = Turtle('square')
        paddle.color("white")
        paddle.penup()
        paddle.speed("fastest")
        paddle.shapesize(stretch_len=5)
        paddle.right(90)
        paddle.goto(position)
        self.paddle_list.append(paddle)

    def move(self, paddle):
        paddle.forward(20)

    def right_up(self):
        self.right_paddle.setheading(UP)

    def right_down(self):
        self.right_paddle.setheading(DOWN)




