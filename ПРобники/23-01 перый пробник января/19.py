def g(s, p, end):
    if s >= 37: return p in end
    if s >= 37: return False
    move = [g(s +1, p+ 1, end), g(s * 2, p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(move)
    else:
        return all(move)
for s in range(1,37):
    if g(s, 0, [2]):
        print(s, '2')
    if g(s,0, [2,4]):
        print(s, '4')