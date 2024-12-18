for a in range(1, 10000):
    f = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((15 * x - 2 * y + 37 != 0) or (a < x) or (a < y)) == False:
                f = False
        if not f:
            break
    else:
        print(a)