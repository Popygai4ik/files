from functools import lru_cache
@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n >= 2:
        return f(n - 1) + 3 * g(n - 1) + n

@lru_cache(None)
def g(n):
    if n == 1:
        return 1
    if n >= 2:
        return 11 * f(n - 1) + g(n - 1) * 2 - n * n

print(f(28)/g(14))

