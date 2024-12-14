for a in range(1, 10000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y + 10*x != 28) or (a > x - 1)) and (a < y + 50)) == False:
                break
        if (((y + 10 * x != 28) or (a > x - 1)) and (a < y + 50)) == False:
            break
    else:
        print(a)