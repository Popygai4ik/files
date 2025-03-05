def dell(n, m):
    return n % m == 0



b = list(range(45, 90+1))
A = []

for a in range(1,1000):
    for x in range(1,100):
        if (dell(x, 52) and (not((not(x in b)) or dell(x, a)))) == True:
            break
    else:
        A.append(a)
print(A)