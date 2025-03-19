def F(n,m):
    if n == 0:
        return m
    if n > 0:
        return F(n // 10, 10 * m + (n % 10))
print(F(4897315885211499052,0))