# for n in range(1,1000):
#
#     bib = bin(n)[2:]
#     k = bib[:2]
#     s2 = bib[::-1]
#     try:
#         zero_pos = s2.index('0')
#         s2 = s2[:zero_pos] + k + s2[zero_pos+1:]
#         bib = s2[::-1]
#         R = int(bib,2)
#         print(n,R)
#     except:
#         pass

for n in range(1, 1000):
    bib = bin(n)[2:]        # Двоичное представление без '0b'
    k = bib[:2]
    k = k[::-1] # Первые две цифры
    s2 = bib[::-1]          # Переворачиваем

    try:
        # Ищем позицию последнего нуля (в перевёрнутой строке — это первый ноль слева)
        zero_pos = s2.index('0')

        # Вставляем k на место этого нуля
        s2 = s2[:zero_pos] + k + s2[zero_pos + 1:]

        # Переворачиваем обратно
        bib_mod = s2[::-1]

        # Переводим обратно в десятичную систему
        R = int(bib_mod, 2)
        # print(f'GH {bin(n)[2:]} N = {n}, R = {R}, mod_bin = {bib_mod} s2 {s2}')
        if R == 227:
            print(f'N = {n}, R = {R}, mod_bin = {bib_mod}')
    except ValueError:
        # Если нет ни одного нуля — пропускаем
        continue
