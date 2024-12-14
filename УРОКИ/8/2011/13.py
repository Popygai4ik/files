# from itertools import *
#
# n = 1
# c = 0
# for i in product(sorted('ДРАЙВЕР'), repeat=5):
#     w = ''.join(i)
#     for k in 'ДРЙР':
#         w = w.replace(k, 'с')
#     if 'сВ' not in w and 'Вс' not in w and sorted(w, reverse=True) == w and len(set(i)) >= 3:
#         c += 1
#         print(w, n)
#     n +=1
# print(c)
from itertools import product

n = 0
c = 0
consonants = set('БВГДЖЗЙКЛМНПРТФХЦЧШЩ')  # Согласные буквы
vowels = set('АЕЁИОУЫЭЮЯ')  # Гласные буквы

for i in product(sorted('ДРАЙВЕ'), repeat=5):
    w = ''.join(i)

    # Условие 1: Рядом с 'В' не должно быть согласных
    if 'В' in w:
        for index in range(len(w)):
            if w[index] == 'В':
                if (index > 0 and w[index - 1] in consonants) or (index < len(w) - 1 and w[index + 1] in consonants):
                    break
        else:
            # Условие 2: Буквы идут в противоположном алфавитном порядке
            if sorted(w, reverse=True) == list(w):
                # Условие 3: Есть хотя бы 3 уникальные буквы
                if len(set(w)) >= 3:
                    c += 1
                    print(w, n)

    n += 1

print(c)

