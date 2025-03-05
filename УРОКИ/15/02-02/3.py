def dell(n, m):
    return n % m == 0


for A in range(1, 19999):
    for x in range(1, 1000):
        if ((A < 77) and ((not(dell(x,A))) <= (dell(x,10)<= (not(dell(x,28)))))) == False:
            break
    else:
        print(A)