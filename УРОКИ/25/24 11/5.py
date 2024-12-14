for i in range(23456, 78954+1):
    d = []
    if i ** 0.5 % 1 != 0:
        continue
    for x in range(2, int(i)):
        if i % x == 0 :
            d.append(x)
            # d.append(i// x)
    d = list(set(d))
    if len(d) == 3:
        print(i, *d)