import sys
sys.setrecursionlimit(10000000)
def f(n):
    if n == 1:
        return n
    if n >1:
        return n * f(n - 1)
print((2026 * f(2029) + f(2028)) / f(2027))