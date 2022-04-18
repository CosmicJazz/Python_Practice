import io
import sys



sys.stdin = io.StringIO("abc\ndef\nquit\n")

_input = input
def input(p = None):
    x = _input(p)
    print(x)
    return x

while True:
    x = input("next? ")
    if x == 'quit':
        break


