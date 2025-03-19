def g(s, p, end):
    if s >= 120:
        return p in end
    if p > max(end):
        return False
    mov = [g(s + 3, p + 1, end), g((s * 4) - 3, p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
print('# 19')
for s in range(1, 120):
    if g(s, 0,[2]):
        print(s, end=' / ')
print()
print('# 20')
for s in range(1, 120):
    if g(s, 0,[3]) and (not(g(s, 0, [1]))):
        print(s, end=' / ')
print()
print('# 21')
for s in range(1, 120):
    if g(s, 0,[2,4]) and (not(g(s, 0, [2]))):
        print(s, end=' / ')