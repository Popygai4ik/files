# def g(s,end,p):
#     if s <= 19:
#         return p in end
#     if  p > max(end):
#         return False
#     mov = [g(s -2 , end,p+1),g(s - 5, end,p+1),g(s //3,end, p +1 )]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1000,19, -1):
#     if g(s,[2,4],0) and not(g(s,[2], 0)):
#         print(s)
# def game(s,end,p):
#     if s >= 37:
#         return p in end
#     if p > max(end):
#         return False
#     mov = [game(s + 1,end,p+1),game(s + 4,end,p+1),game(s * 3,end,p+1)]
#     if (p + 1)% 2 == end[0]%2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,37):
#     if game(s,[2,4],0) and (not(game(s,[2],0))):
#         print(s)
def g(x,s,end,p):
    if (s + x) >= 74:
        return p in end
    if p >= max(end):
        return False
    mov= []
    for i in range(1,min(s,x)+1):
        mov.append(g(min(s,x) + i, max(s,x),end,p + 1))

    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)

x = 9
for s in range(1,65):
    if g(s,x,[2,4],0) and (not(g(s,x,[2],0))):
        print(s)