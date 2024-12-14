def f(n):
    if n == 1:
        return 3
    if n > 1:
        return 4 * f(n -1) - 3 * n
print(f(5))