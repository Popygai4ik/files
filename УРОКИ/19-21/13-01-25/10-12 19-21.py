def g(x, s, p, end):
    if (s + x) >= 65: return p in end
    if (s + x) < 65 and p == max(end): return False
    mov = [g(x + 2, s, p +1, end), g(x* 2, s, p + 1, end),
           g(x, s + 2, p + 1, end),g(x, s* 2, p +1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
x = 3
# for s in range(1, 62):
#     if  g(x, s, 0, [1]):
#         print(s)
print(19)
print([s for s in range(1, 62) if g(x, s, 0, [1])])
print(20)
print([s for s in range(1, 62) if g(x, s, 0, [3])])
print(21)
print([s for s in range(1, 62) if g(x, s, 0, [2, 4])])
