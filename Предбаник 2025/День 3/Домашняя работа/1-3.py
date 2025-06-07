# def g(s,end,p):
#     if s >= 105:
#         return p in end
#     if p > max(end):
#         return False
#     mov = [g(s + 3,end,p+1),g(s + 4,end,p+1),g(s * 2,end,p+1)]
#     if (p + 1) % 2 == end[0]% 2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,105):
#     if g(s,[2,4], 0) and (not(g(s,[2],0))):
#         print(s)
# def g(s,end,p):
#     if s >= 37:
#         return p in end
#     if p > max(end): return False
#     mov = [g(s + 1,end,p+1),g(s * 2,end,p+1)]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,37):
#     if g(s,[2,4],0) and not(g(s,[2], 0)):
#         print(s)
# def g(s,end,p):
#     if s >= 99:
#         return p in end
#     if p > max(end): return False
#     mov = [g(s * 2,end,p+1),g(s + 8,end,p+1)]
#     if (p + 1) % 2 == end[0]%2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,91):
#     if g(s,[2,4],0) and not(g(s,[2],0)):
#         print(s)
def g(s,end,p, last_dep):
    if s >= 43:
        return p in end
    if p > max(end):
        return False
    mov = []
    if last_dep == '+1':
        mov.append(g(s + 2,end,p+1, '+2'))
        mov.append(g(s * 2,end,p+1,'*2'))
    if last_dep == '+2':
        mov.append((s + 1 ,end,p+1,'+1'))
        mov.append(g(s * 2,end,p+1,'*2'))
    if  last_dep == '*2':
        mov.append(g(s + 1, end, p + 1, '+1'))
        mov.append(g(s + 2, end, p + 1, '+2'))
    if  last_dep == '':
        mov.append(g(s + 1, end, p + 1, '+1'))
        mov.append(g(s + 2, end, p + 1, '+2'))
        mov.append(g(s * 2, end, p + 1, '*2'))
    if (p + 1) % 2 == end[0]% 2:
        return any(mov)
    else:
        return all(mov)
print([s for s in range(1,43) if g(s,[2,4], 0,'') and (not(g(s,[2], 0, '')))])