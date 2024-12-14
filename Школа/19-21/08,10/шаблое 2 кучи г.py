# 19
def f(a,b,n):
    if a + b >= 77 or n >2:
        return n == 2
    return any([f(a + 1, b, n +1),f(a *2, b, n +1),f(a, b + 1 , n +1),f(a, b * 2, n +1) ])
for s in range(1, 70):
    if f(7, s,0):
        print('19,', s)
        break
# 20
def f(a,b,n):
    if a + b >= 77 or n >3:
        return n == 3
    if n % 2 == 1:
        return all([f(a + 1, b, n +1),f(a *2, b, n +1),f(a, b + 1 , n +1),f(a, b * 2, n +1) ])
    return any([f(a + 1, b, n +1),f(a *2, b, n +1),f(a, b + 1 , n +1),f(a, b * 2, n +1) ])
for s in range(1, 70):
    if f(7, s,0):
        print('20,', s)
# 21
def f(a,b,n):
    if a + b >= 77 or n >4:
        return n == 2 or n == 4
    if n % 2 == 0:
        return all([f(a + 1, b, n +1),f(a *2, b, n +1),f(a, b + 1 , n +1),f(a, b * 2, n +1) ])
    return any([f(a + 1, b, n +1),f(a *2, b, n +1),f(a, b + 1 , n +1),f(a, b * 2, n +1) ])
for s in range(1, 70):
    if f(7, s,0):
        print('21,', s)
        break