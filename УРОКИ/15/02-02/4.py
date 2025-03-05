def dell(n, m):
    return n % m == 0

for A in range(1, 1999):
    for x in range(1,10000):
        if ((dell(x, A) and dell(x,8)) <= ((not(dell(x,8))) or dell(x,513))) == False:
            break

    else:
        print(A)