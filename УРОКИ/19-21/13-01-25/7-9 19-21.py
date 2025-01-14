def g(s, p, end):
    if s >= 46:
        return p in end
    if s < 46 and p == max(end):
        return False

    mov = [g(s + 2, p + 1, end), g(s * 2, p + 1, end)]

    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)


print([s for s in range(1, 46) if g(s, 0, [2])])
print([s for s in range(1, 46) if g(s, 0, [3])])
print([s for s in range(1, 46) if g(s, 0, [2, 4])])