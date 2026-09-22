from stringart import *

n = 18
k = 6

make_circle(n)

for i in range(n):
    connect(i, i+k)