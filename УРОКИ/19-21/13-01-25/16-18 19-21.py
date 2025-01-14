def g(x, s, p, end):
    if (x + s) >= 105: return p in end
    if (x + s) < 105 and p == max(end): return False
    mov = [g(x+ 4, s,p + 1, end),g(x, s + 4,p + 1, end),
           g(x, s* 3,p + 1, end),g(x* 3, s,p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
x = 4
print([s for s in range(1, 101) if g(x, s, 0, [2])])
print([s for s in range(1, 101) if g(x, s, 0, [3])])

print([s for s in range(1, 101) if g(x, s, 0, [2, 4])])
