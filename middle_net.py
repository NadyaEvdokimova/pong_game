from turtle import Turtle


class MiddleNet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.draw_a_net()

    def draw_a_net(self):
        for y in range(-290, 330, 40):
            self.goto(0, y)
            self.setheading(90)
            self.pendown()
            self.forward(20)
            self.penup()




