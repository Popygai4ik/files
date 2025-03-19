def g(x, s, p, end):
    if (s * x) >= 184:
        return p in end
    if p > max(end):
        return False
    mov = [g(x+1,s,p+ 1, end),g(x,s+1,p+ 1, end),
           g(x*2,s,p+ 1, end),g(x,s*2,p+ 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:

        return all(mov)
x = 2

print('19 - ',*[s for s in range(1,182) if g(x,s,0,[2])])
print('20 - ',*[s for s in range(1,182) if g(x,s,0,[3]) and (not(g(x,s,0,[1])))])
print('21 - ',*[s for s in range(1,182) if g(x,s,0,[2,4]) and (not(g(x,s,0,[2])))])
