

for A in range(1, 1000):
    for x in range(1,1000):
        if ((x & 41 == 0) or ((x & 21 != 0) <= (x & A != 0 ))) == False:
            break
            
    else:
        print(A)