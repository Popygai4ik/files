from math import ceil
def g(x, s, p, end):
    if (s + x) <= 22: return p in end
    if (s + x) > 22 and p == max(end): return False
    mov =  [g(x, s - 1, p + 1, end), g(x, (s + 1) // 2, p + 1, end),

             g(x - 1, s, p + 1, end), g((x + 1) // 2, s, p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
print([s for s in range(100, 12, -1) if g(
    10, s, 0, [2])])

print([s for s in range(100, 12, -1) if g(
    10, s, 0, [2, 4])])
