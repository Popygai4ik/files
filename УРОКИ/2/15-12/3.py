print('x y z w f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((y <= x) <= (z <= w))
                if f == 0:
                    print(x, y, z, w, f)
