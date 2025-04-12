for a in range(0,1000):
    for x in range(0,1000):
        for y in range(0,1000):
            if ((x > a) or (y > a) or ((y - 2*x + 16) != 0)) == False:
                break
        if ((x > a) or (y > a) or ((y - 2 * x + 16) != 0)) == False:
            break
    else:
        print(a)