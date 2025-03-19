def moves(s, step):

    new_states = [(s - 3), (s - 6)]

    if step % 2 == 1:  # Если ход чётный (2-й, 4-й и т. д.), дополнительно продаётся по 1 акции каждым

        new_states = [m - 2 for m in new_states if m - 2 > 0]

    return new_states

def game(s, step=0):

    if any(m <= 10 for m in moves(s, step)):  # Проверка выигрыша за 1 ход

        return 'WIN1'

    if any(game(m, step + 1) == 'WIN1' for m in moves(s, step)):  # Проверка проигрыша за 1 ход

        return 'LOSS1'



# Найти минимальное S, при котором Вера выигрывает сразу после хода Феликса

for s in range(11, 43):

    if game(s) == 'LOSS2':

        print('Результат 19-го:', s)

