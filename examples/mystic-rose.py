from stringart import *


n = 18
make_circle(n)

for i in range(n):
    for j in range(i, n):
        connect(i, j)
