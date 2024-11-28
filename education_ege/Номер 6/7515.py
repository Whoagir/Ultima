from turtle import *
s=15
tracer(0)
for i in range (3):
    forward(7*s)
    right(90)
    forward(12*s)
    right(90)
up()
forward(4*s)
right(90)
forward(6*s)
left(90)
down()
for i in range(4):
    forward(83*s)
    right(90)
    forward(77*s)
    right(90)
for x in range(-50,20):
    for y in range(-80,80):
        up()
        goto(x*s,y*s)
        down()
        dot(3)
exitonclick()