print('x y z w f1 f2')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                 f1 = (w <= z) == (y <= x)
                 f2 = (w <= z) and ((not(x)) == y)
                 if z == 0 and y == 1 and x == 1 and f2 == 0:
                     print(x, y, z, w, int(f1), int(f2))