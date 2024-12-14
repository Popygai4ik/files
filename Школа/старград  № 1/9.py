# f= open('9.txt')
# c = 0
# for i in f:
#     s = list(map(int, i.split()))
#     sr_n = sum(set(s)) / len(set(s))
#     nec = []
#     for j in s:
#         s1 = list(map(str, s))
#         if s1.count(str(j)) > 1:
#             nec.append(j)
#     if len(nec) == 0:
#         sr_p = sr_n
#     else:
#         sr_p = sum(nec)/ len(nec)
#     if len(set(s)) <= 4 and len(set(s)) > 0 and sr_p > sr_n:
#         c += 1
# print(c)
f = open('9.txt')
kolvo = 0

for s in f:
    chisla = list(map(int, s.split()))
    chastota = {chislo: chisla.count(chislo) for chislo in chisla}

    est_tri = any(chast >= 3 for chast in chastota.values())
    est_odno = any(chast == 1 for chast in chastota.values())

    if not (est_tri and est_odno):
        continue

    povtory = [chislo for chislo in chisla if chastota[chislo] > 1]
    if povtory:
        sred_povtory = sum(povtory) / len(povtory)
    else:
        sred_povtory = 0

    unikalnye = [chislo for chislo in chisla if chastota[chislo] == 1]
    if unikalnye:
        sred_unikalnye = sum(unikalnye) / len(unikalnye)
    else:
        sred_unikalnye = 0

    if sred_povtory > sred_unikalnye:
        kolvo += 1

print(kolvo)
