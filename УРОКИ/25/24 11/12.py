from itertools import *
c = 0
for k in range(1, 1000):
    m= 7000000 + k
    dele = []
    for i in range(2, int(m ** 0.5) +1):
        if m % i == 0:
            dele.append(i)
            dele.append(m // i)
    if len(['ДААААААА' for m1, m2, m3 in combinations(dele, r=3) if m1 * m2*m3]) == 0:
        print(k)
        c +=1
    if c == 5:
        break