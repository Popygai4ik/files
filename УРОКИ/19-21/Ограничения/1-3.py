# def g(s, p, end):
#     if 65 <= s <= 100:
#         return  p in end
#     if s > 100 or p > max(end): return False
#     mov = []
#     if s + 1 <= 100: mov.append(g(s + 1, p + 1, end))
#     if s * 3 <= 100: mov.append(g(s * 3, p + 1, end))
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,65):
#     if g(s,0,[2, 4]) and (not( g(s,0,[2]) )) :
#         print(s)
# def g(s, p, end):
#     if 16 <= s <= 22:
#         return  p in end
#     if p > max(end) or s < 16 : return False
#
#     mov = [g(s - 1, p + 1, end)]
#     if s % 2 == 0:
#         mov.append(g(s // 2, p + 1, end))
#     else:
#         mov.append(g((s - 1) // 2, p + 1, end))
#     if ((p + 1) % 2) == (end[0] % 2):
#         return any(mov)
#     else:
#         return all(mov)
# for s in range(1,24):
#     if g(s,0,[2]) :
#         print(s)
def g(s, p, end):
    if 16 <= s <= 22:
        return  p in end
    if p > max(end) or s < 16 : return False

    mov = []
    if (s - 1) > 16 : mov.append(g(s - 1, p + 1, end))
    if (s // 2) >= 16:
        mov.append(g(s // 2, p + 1, end))
    # elif s % 2 != 0 and ((s - 1) // 2) > 16:
    #     mov.append(g((s - 1) // 2, p + 1, end))
    if ((p + 1) % 2) == (end[0] % 2):
        return any(mov)
    else:
        return all(mov)
for s in range(23,10000):
    if g(s,0,[2,4]) and (not( g(s,0,[2]) )):
        print(s)