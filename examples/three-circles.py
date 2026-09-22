from stringart import *

def loop(n, k, color=None):
    if color:
        set_color(color)
    for i in range(n):
        connect(i, i+k)

n = 36

make_circle(n)

loop(n, 16)
loop(n, 13)
loop(n, 9)
