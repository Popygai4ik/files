n, m = [int(input()) for h in range(2)]
rezyltat = 0
while n >= 4 and m >= 4:
    k = min(n, m) // 4
    rezyltat += ((n + m) + (n + m) - 4 * (k - 1)) * k // 2
    n, m = n - 2 * k, m - 2 * k
if n == 3 and m >= 3:
    rezyltat += 2 * m + 1
elif n == 2 and m >= 2:
    rezyltat += m + 1 + int(m >= 3)
elif m == 3 and n >= 3:
    rezyltat += 2 * n + 1
elif m == 2 and n >= 2:
    rezyltat += n + 1
else:
    rezyltat += n * m
print(rezyltat)