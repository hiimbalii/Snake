import turtle
import time

palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)

fej = turtle.Turtle()
fej.penup()
fej.shape("triangle")
fej.color("yellow")

while True:
    palya.update()
    time.sleep(0.3)
