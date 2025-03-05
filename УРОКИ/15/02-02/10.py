def f(a,x,y):
    return ((x < (2 * y)) or (((2 * x + a) <= (3*y)) and (((3 * y) + (2 *y)) > A)))

res = []

for A in range(1,10000):
    for x in range(1,1000):
        for y in range(1, 1000):
            if f(A, x,y) == False:
                break
        if f(A, x, y) == False:
            break
    else:
        res.append(A)
print(len(res))