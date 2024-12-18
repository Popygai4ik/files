def tre(x, y, z):
    a = []
    for i in range(3):
        if i == 0:
            a.append(x)
        elif i ==1:
            a.append(y)
        else:
            a.append(z)
    a.sort()
    return (a[-1])** 2 == (a[0])** 2 + (a[1])** 2
c = 0
for a in range(1, 10000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (tre(16, y, a) or tre(x,y,a) == (x + a < 85)) == False:
                break
        if (tre(16, y, a) or tre(x, y, a) == (x + a < 85)) == False:
            break
    else:
        if a % 2 == 0:
            c += 1
            print(a)
print(c)