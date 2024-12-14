from math import *
for k in range(1, 10000):
    a = 10+52+5000
    i = ceil(log2(a))
    V1 = ceil((i * k) / 8)
    V949 = (V1 * 949) / 1024
    if V949 >= 727:
        print(k)