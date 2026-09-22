from stringart import *

n = 36
k = 12
skip = k-1

make_circle(n)

for i in range(n-skip):
    connect(i, i+k)