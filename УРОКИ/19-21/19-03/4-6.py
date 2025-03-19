def g(s, p, end):
    if s >= 154: return p in end
    if p > max(end):
        return False
    mov = []
    if (s  + 1) % 3 != 0:
        mov.append(g(s + 1, p + 1, end))
    if (s  + 2) % 3 != 0:
        mov.append(g(s + 2, p + 1, end))
    if (s  * 2) % 3 != 0:
        mov.append(g(s * 2, p + 1, end))
    if (p  + 1)  % 2== end[0] % 2:
        return any(mov)
    else:
        return all(mov)
# for s in range(1, 153):
#     if g(s,0,[2]):
#         print('19 - ', s)
for s in range(1, 153):
    if g(s,0,[3]) and s %  3 != 0 and not g(s, 0, [1]) :
        print('20 - ', s)
for s in range(1, 153):
    if g(s,0,[2,4]) and s %  3 != 0 and not g(s, 0, [2]) :
        print('21 - ', s)