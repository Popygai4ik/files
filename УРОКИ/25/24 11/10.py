def is_prime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

pros = [p for p in range(2, 30) if is_prime(p)]
sh = [n for n in range(2, 100, 2)]
rs = []
for m in pros:
    for n in sh:
        N = (2** m)* (5** n)
        if 250_000_000<= N<=1_000_000_000:
            bini = bin(m**2 + n**2)[2:]
            # print(N, bini)
            rs.append([N, bini])
        elif  N > 1_000_000_000:
                break
rs.sort()
for  k in rs:
    print(*k)