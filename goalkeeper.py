from turtle import Turtle

GK_POSITIONS = [(350, 0), (-350, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Goalkeeper(Turtle):

    def __init__(self, player):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(1, 5)
        self.setheading(90)
        self.setpos(GK_POSITIONS[player - 1])
        self.speed("fastest")

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
