def g(s, p, end):
    if s <= 25: return p in end
    if s > 25 and p == max(end): return False
    h = [g(s-1, p +1,end)]
    if s % 2 == 0:
        h.append(g(s // 2, p + 1, end))
    else:
        h.append(g(s - 2, p + 1, end))
    if s % 3 == 0:
        h.append(g(s // 3, p + 1, end))
    else:
        h.append(g(s - 3, p + 1, end))
    if (p + 1) % 2 == (end[0] % 2):
        return any(h)
    else:
        return all(h)

for s in range(26,200):
    if g(s,0,[2, 4]) and not(g(s, 0, [2])):
        print(s)