def f(n):
    if n == 1:
        return 2
    if n > 1:
        return 4*f(n - 1) +2*n
print(f(8))