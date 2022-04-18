import turtle
import random

t = turtle

def main():
    llx = -500
    lly = -500
    urx = 500
    ury = 500
    grass_count = 250

    t.setworldcoordinates(llx, lly, urx, ury)
    t.colormode(255)
    t.up()
    t.setpos(0,-500)
    t.down()
    t.seth(90)

    #Tree(size, angle, speed, width)
    tree(300, 50, 1000, 25)

    t.setpos(500, -500)
    t.setpos(-500, -500)
    for i in range(grass_count+1):
        grass(20, 20, 0, 6)
        t.pencolor(22, random.randrange(50, 120), 8)
        t.setpos(-500 + (i * (urx/grass_count)*2), -500)

    t.exitonclick()

def tree(size, angle, speed, width):
    if size < 10:
        t.width(10)
        t.pencolor(200, random.randrange(50,120), 200)
        t.forward(10)
        t.up()
        t.backward(10)
        t.down()
        t.pencolor(66, 41, 8)
        return 1
    else:
        t.pencolor(66, 41, 8)
        t.width(width)
        t.forward(size)
        t.right(angle)
        tree(size-int(size*random.uniform(.20,.50)), int(angle*random.uniform(1.0, 1.2)), speed, int(width/random.uniform(1.0, 1.5)))
        t.left(angle*2)
        tree(size-int(size*random.uniform(.20,.50)), int(angle*random.uniform(1.0, 1.2)), speed, int(width/random.uniform(1.0, 1.5)))
        t.width(width)
        t.right(angle)
        t.backward(size)

def grass(size, angle, speed, width):

    if size < 4:
        return 1
    else:
        t.down()
        t.seth(90)
        t.width(width)
        t.right(angle * random.randrange(-2, 2))
        t.forward(size)
        grass(size-int(size*random.uniform(.20,.50)), int(angle*random.uniform(1.0, 1.2)), speed, int(width/random.uniform(1.0, 1.5)))
        t.up()

main()