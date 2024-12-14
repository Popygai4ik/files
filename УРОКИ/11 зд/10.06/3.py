from math import *
for N in range(1, 10000):
    k = 283
    i = ceil(log2(N))
    V1 = ceil(k * i)
    v65536 = (V1*65536)/(8*1024*1024)
    if v65536 > 15:
        print(N)