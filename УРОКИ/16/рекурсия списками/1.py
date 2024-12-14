def f(n):
    if n < 3:
        return 1
    if n > 3:
        return f(n - 2) * (n // 3)
print((f(16)))