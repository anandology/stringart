from stringart import *

def one_to_all(n, k):
    for i in range(n):
        connect(i, k)

n = 36
make_circle(n)

one_to_all(n, 18)
one_to_all(n, 15)
one_to_all(n, 21)
