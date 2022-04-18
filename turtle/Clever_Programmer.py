import turtle
import random

t=turtle
width = 1
angle = 89
speed = 100
color = 255
red = 1

def square(width, angle, speed):

    t.width(width)
    t.speed(speed)
    t.forward(100)
    t.right(angle)
    t.forward(100)
    t.right(angle)
    t.forward(100)
    t.right(angle)
    t.forward(100)

#t.up()
#t.left(90)
#t.forward(100)
#t.left(90)
#t.forward(100)
#t.right(180)
#t.down()

for count in range(360):

    print(random.uniform(1.0,1.5))
    #square(width, angle, speed)

t.exitonclick()
