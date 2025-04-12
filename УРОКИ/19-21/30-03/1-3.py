def g(s,p,end):
    if s == 0: return p in end
    if p >= max(end): return False
    mov = [g(s // 5,p +1, end)]
    if s >= 5: mov.append(g(s - 5,p +1, end))
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
# for s in range(1,1000):
#     if g(s,0,[2]) and not (g(s, 0, [1])):
#         print(s)
for s in range(1,1000):
    if g(s,0,[2,4]) and not (g(s, 0, [2])):
        print(s)