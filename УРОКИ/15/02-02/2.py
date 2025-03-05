def dell(n, m):
    return n % m == 0


for A in range(1, 19999):
    for x in range(1, 1000):
        if (dell(x,A) <= (dell(x,7)) or dell(x,70)) == False:
            break
    else:
        print(A)