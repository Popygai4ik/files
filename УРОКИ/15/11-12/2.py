for a in range(1, 10000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if ((15*x - y + 40 != 0)or (a < x) or (a < y)) == False:
                break
        if ((15 * x - y + 40 != 0) or (a < x) or (a < y)) == False:
            break
    else:
        print(a)








