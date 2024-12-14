# f = open('170.txt')
# kolvo = 0
#
# for s in f:
#     chisla = list(map(int, s.split()))
#     chastota = {chislo: chisla.count(chislo) for chislo in chisla}
#
#     est_dva = any(chast == 2 for chast in chastota.values())
#
#     if not (est_dva):
#         continue
#
#     povtory = [chislo for chislo in chisla if chastota[chislo] == 2]
#     if len(povtory) != 1:
#         sred_povtory = sum(povtory)
#     else:
#         sred_povtory = 0
#
#     unikalnye = [chislo for chislo in chisla if chastota[chislo] == 1]
#     if unikalnye:
#         sred_unikalnye = sum(unikalnye) / len(unikalnye)
#     else:
#         sred_unikalnye = 0
#
#     if sred_unikalnye <= sred_povtory:
#         kolvo += 1
#
# print(kolvo)
f = open('170.txt')
kolvo = 0

for s in f:
    chisla = list(map(int, s.split()))
    chastota = {chislo: chisla.count(chislo) for chislo in chisla}

    povtory = [chislo for chislo, count in chastota.items() if count == 2]
    if len(povtory) >1 or len(povtory) == 0:
        continue

    suma_povtory = povtory[0] * 2

    unikalnye = [chislo for chislo, count in chastota.items() if count == 1]
    if len(unikalnye) + 2 != 6:
        continue
    if unikalnye:
        sred_unikalnye = sum(unikalnye) / len(unikalnye)
    else:
        sred_unikalnye = 0

    if sred_unikalnye <= suma_povtory:
        kolvo += 1

print(kolvo)
