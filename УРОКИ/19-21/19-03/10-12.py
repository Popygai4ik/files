def g(s,p,end):
    if s < 15: return p in end
    if p > max(end):
        return False
    mov = [g(s - 1, p +1, end)]
    if s % 2 == 0:
        mov.append(g(s // 2, p +1, end))
    if s % 5 == 0:
        mov.append(g(s - 0.2 * s, p +1, end))
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
for s in range(15, 1000):
    if g(s, 0, [2,4]) and (not(g(s,0,[2]))):
        print(s)