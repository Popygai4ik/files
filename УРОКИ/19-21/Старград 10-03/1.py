def g(s, p,end):
    if s <= 19: return p in end
    if p > max(end):
        return False
    mov =[g(s-1,p+1,end)]
    if s % 3 == 0:
        mov.append(g(s//3,p+1,end))
    else:
        mov.append(g(s-2,p+1,end))
    if s % 5 == 0:
        mov.append(g(s // 5,p +1, end))
    else:
        mov.append(g(s-3,p+1,end))
    if (p + 1)% 2 == end[0]% 2:
        return any(mov)
    else:
        return all(mov)

for s in range(1000,1,-1):
    if g(s,0,[2]):
        print(s)
print('213123123')
for s in range(1000,1,-1):
    if g(s,0,[3]) and (not(g(s,0,[1]))):
        print(s)
print('213123123')
for s in range(1000,1,-1):
    if g(s,0,[2,4]):
        print(s)