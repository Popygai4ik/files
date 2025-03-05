def inf(x,y,z):
    a = [x,y,z]
    a.sort()
    if (a[0]+a[1]) > a[-1]:
        return x == y == z
    return False
def f(a,x, y):
    return ((a > 30) <= ((inf(40,y,A)) <= (inf(x,y,A))))

res = []
for A in range(1, 1000):
    for x in range(1, 100):
        for y in range(1, 100):
            if f(A, x, y) == False:
                break
        if f(A, x, y) == False:
            break
    else:
        # print(A)
        res.append(A)
print(len(res))

