import turtle

t = turtle

def tree(size, angle):
    if size < 0:
        return 1
    else:
        t.forward(size)
        t.right(angle)



def main():
    t.left(90)
    t.backward(300)
    t.speed(0)
    tree(75, 20)
    t.exitonclick

main()
