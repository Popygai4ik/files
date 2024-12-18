for a in range(1, 10000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y + 5 * x != 31) or (a > x - 2)) and (a, y + 37)) == False:
                flag = False
                break
        if not flag:
            break
    else:
        print(a)