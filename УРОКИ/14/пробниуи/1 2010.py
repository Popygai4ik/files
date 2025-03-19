def to5(n):
    res = ''
    while n > 0:
        res += str(n % 5)
        n = n //5
    return res[::-1]
print(str(to5(5 **260 - 5**160 + 5 ** 60 - 5 ** 46 + 6)).count('0'))