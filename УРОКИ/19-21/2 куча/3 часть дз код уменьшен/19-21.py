def g(x,s,p,end):
    if (x + s) >= 80: return p in end
    if (x  + s) < 80 and p == max(end): return False
    mov = [g(x + 1, s, p + 1, end),g(x * 3, s, p + 1, end),
           g(x, s + 1 , p + 1, end),g(x, s* 3, p + 1, end)]
    if (p + 1)% 2 == (end[0] % 2):
        return any(mov)
    else:
        return all(mov)
# def g1(x, s, p, end):
#     if (x + s) >= 80 and p in end:
#         return True
#     if (x + s) < 80 and p == max(end):
#         return False
#     if (x + s) >= 80 and p not in end:
#         return False
#     if ((p +1) % 2) == (end[0] % 2):
#         return g(x, s + 2, p + 1, end) or g(x, s * 3, p + 1, end) or g(x + 2, s, p + 1, end) or g(x * 3, s, p + 1, end)
#     else:
#         return (g(x + 2, s, p + 1, end) and g(x * 3, s, p + 1, end) and g(x, s + 2, p + 1, end) and g(x, s * 3, p + 1, end))
# x = 10
# for s in range(1, 79):
#     if g(x, s, 0, [2, 4]) and (not(g(x, s, 0, [2]))):
#         print(s)
# x = 3
# for s in range(1, 77):
#     if g(x, s, 0, [2, 4]) and (not(g(x, s, 0, [2]))):
#         print(s)
# def g1(s, p, end):
#     if s >= 150: return p in end
#     if s < 150 and p == max(end): return False
#     mov = [g1(s + 3, p +1, end),g1(s* 2, p +1, end)]
#     if (p + 1) % 2 == end[0] % 2:
#         return any(mov)
#     else:
#         return all(mov)
#
# res = []
# for s in range(1, 126):
#     if g1(s, 0, [2, 4]) and (not(g1(s, 0, [2]))):
#         print(s)
        # res.append(s)
# print(sum(res))
def g1(s, p, end):
    if s >= 68: return p in end
    if s <= 68 and p == max(end): return False
    mov = [g1(s - 1, p +1, end),g1(s - 3, p  +1, end), g1(s - 7, p +1, end), g1(s - (s //2 ), p +1, end)]
    if (p + 1)% 2 == end[0] % 2:
        return any(mov)
    else:
        return any(mov)
for s in range(1, 1000):
    if g1(s, 0, [2]):
        print(s)
