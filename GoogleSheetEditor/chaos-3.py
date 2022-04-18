#   chaos-3.py
#
#  Build Feigenbaum Logistic map. Input start and end K
#
#  python chaos-3.py 3.4 3.9
#


canWidth = 1920
canHeight = 1080


def setupWindow():
    global win, canvas
    from tkinter import Tk, Canvas, Frame
    win = Tk()
    canvas = Canvas(win, height=canHeight, width=canWidth)
    f = Frame(win)
    canvas.pack()
    f.pack()


def startApp():
    global win, canvas
    import sys
    k1 = float(sys.argv[1])  # starting value of K
    k2 = float(sys.argv[2])  # ending   value of K
    x = .2  # is somewhat arbitrary
    vrng = range(200)  # We'll do 200 horz steps
    for t in range(canWidth):
        win.update()
        k = k1 + (k2 - k1) * t / canWidth
        print
        "K = %.04f" % k
        for i in vrng:
            p = x * canHeight
            canvas.create_line(t, p, t, p + 1)  # just makes a pixel dot
            x = x * (1 - x) * k  # next x value
            if x <= 0 or x >= 1.0:
                print
                "overflow at k", k
                return


def main():
    setupWindow()  # Create Canvas with Frame
    startApp()  # Start up the display
    win.mainloop()  # Just wait for user to close graph


if __name__ == "__main__": main()