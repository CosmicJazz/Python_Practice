# chaos-1.py
import sys

k = float(sys.argv[1])
x = float(sys.argv[2])
for i in range(300):
    print("%.06f" % x)
    x = x * (1.0-x) * k