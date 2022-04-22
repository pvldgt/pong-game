from turtle import Turtle, Screen


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()
        self.screen = Screen()
        self.player_names = self.screen.textinput("Enter your names", "Left Player, Right Player")
        self.left_player, self.right_player = self.player_names.split(",")

    def score_up(self, side):
        # count the score of the left and right player and update the score
        if side == "l_score":
            self.l_score += 1
        elif side == "r_score":
            self.r_score += 1
        self.update_score()

    def update_score(self):
        # clear the previous screen and display the score
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def win(self):
        # display the winner's name at the end of the game
        self.color("red")
        self.goto(0, 0)
        if self.l_score > self.r_score:
            self.write(f"{self.left_player} WON", align="center", font=("Courier", 60, "bold"))
        else:
            self.write(f"{self.right_player} WON", align="center", font=("Courier", 60, "bold"))






