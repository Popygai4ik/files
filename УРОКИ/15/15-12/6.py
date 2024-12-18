for a in range(1, 10000):
    for x in range(0, 10000):
        if ((x & a != 0)<= ((x & 31 == 0)<= (x & 61 != 0))) == False:
            break
    else:
        print(a)