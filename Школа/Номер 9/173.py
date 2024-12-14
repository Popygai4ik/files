# from math import sqrt
#
# f = open('170.txt')
# kolvo = 0
#
# for s in f:
#     chisla = list(map(int, s.split()))
#     chastota = {chislo: chisla.count(chislo) for chislo in chisla}
#
#     est_tri = any(chast >= 4 for chast in chastota.values())
#
#     if not (est_tri ):
#         continue
#
#     povtory = [chislo for chislo in chisla if chastota[chislo] >=4]
#
#
#     unikalnye = [chislo for chislo in chisla if chastota[chislo] == 1]
#     if len(unikalnye) !=2 :
#         continue
#
#     if sqrt(povtory[0]**4) >= unikalnye[0] * unikalnye[1]:
#         kolvo += 1
#
# print(kolvo)
from math import sqrt

f = open('170.txt')
kolvo = 0

for s in f:
    chisla = list(map(int, s.split()))
    chastota = {chislo: chisla.count(chislo) for chislo in chisla}

    povtory = [chislo for chislo, count in chastota.items() if count > 1]

    unikalnye = [chislo for chislo, count in chastota.items() if count == 1]

    if len(unikalnye) != 2:
        continue

    if len(povtory) > 0:

        произведение = 1
        количество = 0

        for chislo in povtory:
            количество += chastota[chislo]
            произведение *= chislo ** chastota[chislo]
        srednee_geometricheskoe = произведение ** (1 / количество)

        proizvedenie_unikalnye = unikalnye[0] * unikalnye[1]

        if srednee_geometricheskoe >= proizvedenie_unikalnye:
            kolvo += 1

print(kolvo)
