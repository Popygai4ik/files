for a in range(0, 10000):
    for x in range(0, 1000):
        for y in range(0, 1000):
            if (((x > 15) <= (x * y + 10*x>= a)) and ((y * x  + y > a)<= (y >= 1))) == False:
                break
        if (((x > 15) <= (x * y + 10 * x >= a)) and ((y * x + y > a) <= (y >= 1))) == False:
            break
    else:
        print(a)