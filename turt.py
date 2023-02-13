import turtle
import random
import math

max = turtle.Turtle()
max.color('blue','orange')
max.begin_fill()

for i in range(100):
    max.forward(100)
    max.left(math.pi * 20)
max.end_fill()

turtle.done()