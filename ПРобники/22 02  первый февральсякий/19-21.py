def f(s, x,p, end):
    if (s + x) >= 234: return p in end
    if (s + x) < 234 and max(end)==p: return False
    mof = [f(s+1,x,p+1,end),
           f(s*5,x,p+1,end),
           f(s,x+1,p+1,end),
           f(s,x*5,p+1,end)]
    if (p + 1)% 2 == end[0]%2:
        return any(mof)
    else:
        return all(mof)
x = 7
for s in range(1, 100):
    if f(s,x,0,[2]):
        print(s, 2)
    if f(s,x,0,[2, 4]):
        print(s, 4)