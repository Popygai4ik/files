def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - g(n - 1) - n


def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) - g(n - 1) + 1
print(f(15) + g(15))
