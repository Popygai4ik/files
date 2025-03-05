
for A in range(1, 1000):
    for x in range(1 ,1000):
        if ((x & A != 0) <= ((x & 15 != 0) <= (x & 30 != 0))) == False:
            break

    else:
        print(A)