from turtle import Turtle
from math import cos

t = Turtle()
t.shape("turtle")


for x in range(50):
    t.pensize(100*cos(1))
    t.forward(10*x)
    t.right(40)

input("Press any key to exit")