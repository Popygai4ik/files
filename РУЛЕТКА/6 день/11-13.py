def g(s,p,end, last_mov):
    if s >= 21: return p in end
    if p >= max(end): return False
    moves = []

    # Петя не может повторить свой прошлый ход
    if last_mov != '+1':
        moves.append((s + 1, '+1'))
    if last_mov != '+2':
        moves.append((s + 2, '+2'))
    if last_mov != '*2':
        moves.append((s * 2, '*2'))

    if p % 2 == 0:
        return any(g(new_s, p + 1, end, move) for new_s, move in moves)
        # Ход Вани
    else:
        return all(g(new_s, p + 1, end, move) for new_s, move in moves)
for s in range(1, 21):
    if g(s,0,[5], '') and not (g(s, 0, [3], '')) and not (g(s, 0, [1], '')):
        print(s)