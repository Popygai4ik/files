def f(n):
    if n == 1:
        return 1
    if n % 2 == 0 and n > 1:
        return f(n -1) + 13
    if n % 2 != 0 and n > 1:
        return 2 * f(n -2) + 2 * n * n
print(f(100))