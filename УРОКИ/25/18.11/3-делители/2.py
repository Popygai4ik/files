for n in range(14620, 15001):
    deli = []
    for i in range(2, n):
        if n % i == 0:
            deli.append(i)
    # print(deli)
    if len(deli) == 3:
        print(n, min(deli))