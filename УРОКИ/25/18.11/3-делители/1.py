for n in range(200123, 200151):
    deli = []
    for i in range(1, n + 1):
        if n % i == 0:
            deli.append(i)
    # print(deli)
    if len(deli) == 4:
        print(*deli)