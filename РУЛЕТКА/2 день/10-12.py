def g(x,s,p,end):
    if (x + s) <= 22:
        return p in end
    if p > max(end): return False
    mov = [g(x - 1, s, p + 1, end),
           g(x, s - 1, p + 1, end)]
    if x % 2 == 0:
        mov.append(g(x//2,s, p + 1, end))
    else:
        mov.append(g((x // 2) + 1, s, p + 1, end))
    if s % 2 == 0:
        mov.append(g(x,s//2, p + 1, end))
    else:
        mov.append(g(x, (s // 2)+1, p + 1, end))
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
x = 10
for s in range(13,1000):
    if g(x,s,0,[2,4]) and (not(g(x,s,0,[2]))):
        print(s)
