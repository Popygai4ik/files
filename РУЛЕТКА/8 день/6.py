def f(n):
    if n>= 2025:
        return n * n
    if n < 2025:
        return f(n + 3) + n // 4
print(f(2012)- f(2016))