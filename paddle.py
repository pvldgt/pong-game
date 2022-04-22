from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=5)
        self.right(90)
        self.goto(position)

    def move(self):
        self.forward(20)

    def up(self):
        if self.ycor() < 300:
            self.setheading(UP)
            self.move()

    def down(self):
        if self.ycor() > -300:
            self.setheading(DOWN)
            self.move()
