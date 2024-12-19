print('x y z f')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = ((y or x) <= (z == y))
            if f == 0:
                print(x, y,z, f)