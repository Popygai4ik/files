def f(n):
    if n == 5:
        return n * 5
    if n > 5:
        return (2 + f(n - 1) + 6 * g(n - 1))
def g(n):
    if n == 5:
        return n * 5
    if n > 5:
        return f(n - 1) - g(n - 1) + n*g(n - 1)
print(g(18))
