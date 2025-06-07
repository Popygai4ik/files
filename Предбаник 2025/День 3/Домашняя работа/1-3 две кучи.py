# def g(x,s,end,p):
#     if (s + x) >= 41:
#         return p in end
#     if p > max(end): return False
#     mov = [g(x + 1,s,end,p + 1),g(x,s + 1,end,p + 1),
#            g(x * 2,s,end,p + 1), g(x,s * 2,end,p + 1)]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# x = 13
# for s in range(1,28):
#     if g(x,s,[2,4],0) and (not(g(x,s, [2], 0))):
#         print(s)
# def g(x,s,end,p):
#     if (x + s) >= 105: return p in end
#     if p > max(end): return False
#     mov = [g(x + 4,s,end, p + 1), g(x,s + 4,end, p + 1),
#            g(x * 3,s,end, p + 1),         g(x,s * 3,end, p + 1), ]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# x = 4
# for s in range(1,100+1):
#     if g(x,s,[2,4],0) and (not((g(x,s,[2],0)))):
#         print(s)

# def g(x,s,end,p):
#     if (s + x) >= 63:
#         return p in end
#     if p >= max(end): return False
#     mov = []
#     for i in range(1,min(x,s)+1):
#         mov.append(g(min(x,s) + i, max(s,x),end,p + 1))
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# x = 7
# for s in range(1,56):
#     if g(x,s,[2,4],0) and (not(g(x,s,[2],0))):
#         print(s)
#
# def g(x,s,end,p):
#     if (s+x) <= 40:
#         return p in end
#     if p >= max(end):
#         return False
#     mov = [g(x - 1,s,end,p + 1),g(x,s - 1,end,p + 1)
#            ,g(x // 2,s,end,p + 1),g(x,s//2,end,p + 1)]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# x = 6
# for s in range(200,0,-1):
#     if  g(x,s,[2,4],0) and (not(g(x,s,[2], 0))):
#         print(s)

def g(x,s,end,p):
    if (s + x) > 150:
        return p in end
    if p >= max(end):
        return False
    mov = [g(s + 3,x + 3,end, p+ 1),g(s*2,x,end, p+ 1),g(s,x * 2,end, p+ 1)]
    if (p + 1) % 2 == end[0]%2:
        return any(mov)
    else:
        return all(mov)
x = 7
for s in range(2,143):
    if g(s,x,[2,4],0) and (not(g(x,s,[2],0))):
        print(s)