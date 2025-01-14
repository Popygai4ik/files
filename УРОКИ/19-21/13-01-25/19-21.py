def g(s, p, end):
    if s >= 155: return p in end
    if s < 155 and p == max(end): return False
    mov = [g(s + 4, p + 1, end), g(s* 2, p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)

print([s for s in range(1, 141) if g(s, 0, [2])])
print([s for s in range(1, 141) if g(s, 0, [2, 4])])