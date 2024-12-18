for a in range(0, 10000):
    f = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((3 * y - x < a) or (x >= 35) or (y >= 51)) == False:
                f = False
                break
        if not f:
            break
    else:
        print(a)