from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.position = position
        self.goto(self.position)

    def up(self):
        if self.ycor() < 240:
            y_current = self.ycor()
            self.sety(y_current + 20)

    def down(self):
        if self.ycor() > - 240:
            y_current = self.ycor()
            self.sety(y_current - 20)