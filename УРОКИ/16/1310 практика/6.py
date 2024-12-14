from functools import lru_cache
def sum_digits(n):

    s = 0

    for i in str(n):

        s += int(i)

    return s
@lru_cache()
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 3 * f(n - 1) + 2* g(n - 1) + n*n
@lru_cache()
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * f(n - 1) + 3 * g(n - 1) + n * 5

print(abs(sum_digits(g(222)) - sum_digits(f(333))))