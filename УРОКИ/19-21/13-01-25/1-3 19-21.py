def g(s, p, end):
    if s >= 54: return p in end
    if s < 54 and p == max(end): return False
    mov = [g(s * 3 , p + 1, end), g(s + 2, p + 1, end), g(s + 1 , p + 1, end)]
    if (p + 1) % 2 == end[0] % 2:
        return any(mov)
    else:
        return all(mov)
# for s in range(1, 54):
#     if g(s, 0, [1]):
#         print(f'19 {s}')
#     if g(s, 0, [3]):
#         print(f'20 {s}')
print([s for s in range(1, 54) if g(s, 0, [2, 4])])
print([s for s in range(1, 54) if g(s, 0, [2])])
