def f(a, x, y):
    return (((y - 4*x) < A) or (x > 60) or (y > 10))

for A  in range(1,1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(A,x,y) == False:
                break
        if f(A, x, y) == False:
            break
    else:
        print(A)