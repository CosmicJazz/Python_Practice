#  chaos-2.py
#
#  Make 2 plots x,t that start close together
#
#  python chaos-2.py 3.7  # floating value for k (try 2.1 2.5 2.7 2.9 3.7)
#
import sys
import matplotlib.pyplot as plt

def nextX (k,x) :
    return x * (1.0-x) * k

def main() :
    k = float(sys.argv[1])
    plt.suptitle("k is %f" % k, size=16)

    tims, vals = valsByTime(k, 0.35, 50)
    plt.plot(tims, vals, 'r')

    tims, vals = valsByTime(k, 0.34, 50)
    plt.plot(tims, vals, 'b')
    plt.show()

def valsByTime (k, x, nSteps) :
    tims = range(nSteps)
    vals = []
    for i in tims :
        xp = nextX(k,x)
        vals.append(xp)
        x = xp
    return tims, vals

if __name__ == "__main__" : main()