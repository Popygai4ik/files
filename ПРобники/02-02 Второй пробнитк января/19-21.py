def g(x,s,p,end):
    if (x + s) >= 117: return p in end
    if (x  + s) < 117 and p == max(end): return False
    mov = [g(x + 3, s, p + 1, end),g(x * 3, s, p + 1, end),
           g(x, s + 3 , p + 1, end),g(x, s* 3, p + 1, end)]
    if (p + 1)% 2 == (end[0] % 2):
        return any(mov)
    else:
        return all(mov)
x = 7
print([s for s in range(1, 110) if g(x, s, 0, [2])])
print([s for s in range(1, 110) if g(x, s, 0, [3])])
print([s for s in range(1, 110) if g(x, s, 0, [2, 4])])
