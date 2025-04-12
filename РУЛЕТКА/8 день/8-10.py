def g(s,p,end):
    if s < 25:
        return p in end
    if p > max(end):
        return False
    mos = [g(s-1,p+1,end),g(s-2,p+1,end)]
    if s % 2 == 0:
        mos.append(g(s//2,p+1,end))
    if s % 3 == 0:
        mos.append(g(s - s*(1/3),p+1,end))
    if (p+1)% 2 == end[0] % 2:
        return any(mos)
    else:
        return all(mos)
def g1(s, p, end):
    if s < 25:
        return p in end  # победа, если ход в списке "победных"

    if p > max(end):
        return False
    # print('123')
    moves = [g(s - 1, p + 1, end), g(s - 2, p + 1, end)]

    if s % 2 == 0:
        moves.append(g(s // 2, p + 1, end))
    if s % 3 == 0:
        moves.append(g(s - s // 3, p + 1, end))

    if (p + 1) % 2 == end[0] % 2:  # следующий игрок на победе — хотим хоть один выигрыш
        return any(moves)
    else:
        return all(moves)

for s in range(25,1000):
    if g(s, 0,[2,4]) and (not(g(s, 0, [2]))):

        print(s)
for s in range(25,1000):
    if g1(s, 0,[2,4]) and (not(g1(s, 0, [2]))):

        print(s)
