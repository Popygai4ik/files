for a in range(0, 10000):
    f = True
    for x in range(1, 100):
        for y in range(1, 100):
            if ((((y > a) or (x*y < 2*a)) <= (a * y < 30)) or ((2*y+4*x)<a)) == False:
                f = False
        if not f:
            break
    else:
        print(a)