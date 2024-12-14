shirina = int(input())
dlina = int(input())
p = (lambda x, y: ((x // y) * x + (y // x) * y) // (x // y + y // x))(shirina, dlina)
q = p - (shirina + dlina - p - 1) // 2 * 2
r = 2 - (shirina + dlina - p) % 2
print(q * r)