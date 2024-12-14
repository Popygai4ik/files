for a in range(1, 1000):
    for x in range(1, 1000):
        if ((x & 45 != 0) <= ((x & 23 == 0)<= (x & a != 0))) == False:
            break
    else:
        print(a)