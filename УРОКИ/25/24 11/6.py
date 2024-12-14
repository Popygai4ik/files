for i in range(400000 +1, 400000 +1 +1000):
    M = 0
    for d in range(2, i):
        if i % d == 0:
            m = d + i // d
            break
    if m % 10 == 8:
        print(i)