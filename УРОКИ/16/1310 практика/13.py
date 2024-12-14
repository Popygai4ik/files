import sys
sys.setrecursionlimit(10000)
def f(m, n):
    if m == 0:
        return n + 1
    if n == 0 and m > 0:
        return f(m -1, 1)
    if n > 0 and m > 0:
        return f(m -1,f(m, n -1))
print(f(4,1))