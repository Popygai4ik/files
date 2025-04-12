def g(x,s,p,end):
    if (x + s) > 185:
        return p in end
    if p > max(end):
        return False
    mov = [g(x+2,s+2,p + 1,end),g(x*3,s,p + 1,end),g(x,s*3,p + 1,end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return any(mov)
x = 7
for s in range(1,178):
    if g(x,s,0,[2]):
        print(s)