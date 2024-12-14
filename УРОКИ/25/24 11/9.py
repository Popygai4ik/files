def is_prime(number):
    # if number is equal to or less than 1, return False
    if number <= 1:
        return False

    for x in range(2, number):
        # if number is divisble by x, return False
        if number % x == 0:
            return False
    return True

for i in range(600001, 600000 +1000):
    d = []
    c= 0
    for z in range(1, int(i ** 0.5)):
        if i % z == 0:
            d.append(z)
            d.append(i// z)
            if is_prime(z):
                c += 1
            if is_prime(i // z):
                c +=1
    if not(is_prime(len(d))) and c %  2 == 0:
        print(i, c)