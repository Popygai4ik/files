from fnmatch import fnmatch
def is_prime(number):
    # if number is equal to or less than 1, return False
    if number <= 1:
        return False

    for x in range(2, number):
        # if number is divisble by x, return False
        if number % x == 0:
            return False
    return True
for i in range(0, 10**9, 74):
    if fnmatch(str(i), '5*1?*1?*'):
        if i % 13 != 0:
            cn = 0
            for x in range(1, i):
                if i % x == 0 and is_prime(x):
                    cn +=1
            if cn >= 6:
                print(i)
