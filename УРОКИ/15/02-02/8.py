def f(a, x, y):
    return (((3 * x - y) < A) or ((x + 3 * y) > 45) or ((3 *x + y) < 35))

for A  in range(1,1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(A,x,y) == False:
                break
        if f(A, x, y) == False:
            break
    else:
        print(A)