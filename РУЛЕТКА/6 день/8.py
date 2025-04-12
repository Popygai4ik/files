from functools import *
@lru_cache(None)
def f(n):
    if n == 0:
        return 1
    if n > 0:
        return f(n - 1)* n
res = 0
for n in range(1,10_555_555+1):
    s  = str(f(n))[-4:]
    res = max(res, sum(int(t) for t in s))
print(res)