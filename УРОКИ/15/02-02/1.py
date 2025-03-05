def dell(n, m):
    return n % m == 0


for A in range(1, 19999):
    for x in range(1, 1000):
        if ((not(dell(x, A))) <= (dell(x, 12) <= (not(dell(x,3))))) == False:
            break
    else:
        print(A)