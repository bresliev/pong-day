from turtle import  Turtle, Screen
from goalkeeper import Goalkeeper
from ball import Ball

players = []

# this was same
pong_screen = Screen()
pong_screen.setup(width=800, height=600)
pong_screen.bgcolor("black")
pong_screen.listen()
pong_screen.tracer(0)

def separate_screen():
    separater_turtle = Turtle()
    separater_turtle.color("white")
    separater_turtle.penup()
    separater_turtle.hideturtle()
    separater_turtle.setpos((0, -280))
    separater_turtle.setheading(90)
    separater_turtle.pensize(5)

    while separater_turtle.ycor() < 280:
        separater_turtle.pendown()
        separater_turtle.forward(10)
        separater_turtle.penup()
        separater_turtle.forward(20)


pong_screen.update()
separate_screen()
players.append(Goalkeeper(1))
players.append(Goalkeeper(2))
ball = Ball()


#move the human player up and down
pong_screen.onkey(key="Up", fun=players[0].up)
pong_screen.onkey(key="Down", fun=players[0].down)

pong_screen.onkey(key="W", fun=players[1].up)
pong_screen.onkey(key="S", fun=players[1].down)

is_game_on = True

while is_game_on:
    pong_screen.update()
    ball.move()

pong_screen.exitonclick()