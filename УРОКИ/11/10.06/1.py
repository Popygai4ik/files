from math import *
for k in range(1, 10000):
    N = 10+52+980
    i = ceil(log2(N))
    V1 = ceil((i * k) / 8)
    V385 = (385 * V1) / 1024
    if V385 <= 136:
        print(k)