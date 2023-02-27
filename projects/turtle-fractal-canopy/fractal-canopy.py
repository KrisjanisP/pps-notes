from turtle import *
import random

WIDTH, HEIGHT = 500, 400
setup(WIDTH, HEIGHT)
speed("fastest")
hideturtle()

def branch(level):
    pencolor((139+level*10)/255,(69+level*10)/255,(19+level*10)/255)
    width(6-level/2)
    forward(40-2*level+random.randint(-level, level))
    if level>8:
        pencolor(0,0.8,0)
        circle(2)
        return
    x, y = xcor(), ycor()
    angle = heading()
    left(20+random.randint(-16, 16))
    branch(level+1)
    up()
    goto(x,y)
    down()
    setheading(angle)
    right(20+random.randint(-16, 16))
    branch(level+1)
up()
goto(0, -HEIGHT/2+10)
down()
setheading(90)
branch(1)
done()
