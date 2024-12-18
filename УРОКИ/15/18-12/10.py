def ygl(a, b, c):
    return (a + b+ c) == 180
for a in range(1, 1000):
    for x in range(1, 1000):
        if (ygl(47, a, x + 40) == (ygl(a, x, 45) and (not(a + 30 < 156)))) == False:
            break
    else:
        print(a)