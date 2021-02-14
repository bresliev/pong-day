from turtle import Turtle
from time import

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setpos(0,0)
        self.color("white")
        self.shape("circle")
        self.shapesize(1, 1)
        self.left(38)
        self.speed("slow")

    def first_move(self):
        if self.xcor() <  345:
            self.forward(10)

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)


