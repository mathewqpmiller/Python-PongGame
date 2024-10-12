from turtle import Screen, Turtle


turtle = Turtle()
screen = Screen()
turtle.color("white")
turtle.penup()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")


screen.exitonclick()
