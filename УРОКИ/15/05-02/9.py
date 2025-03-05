d = list(range(30,45+1))
def dell(n,m):
    return n % m == 0
for a in range(1,1000):
    for x in range(1,1000):
        if (((not(dell(x,6))) and (x not in [45, 50, 55, 60])) <= ((abs(x - 15) <= 5) <= (x in d)) or (x & a != 0)) == False:
            break
    else:
        print(a)