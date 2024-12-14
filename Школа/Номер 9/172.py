f = open('170.txt')
kolvo = 0

for s in f:
    chisla = list(map(int, s.split()))
    chastota = {chislo: chisla.count(chislo) for chislo in chisla}

    est_tri = any(chast == 2 for chast in chastota.values())

    if not (est_tri ):
        continue

    povtory = [chislo for chislo in chisla if chastota[chislo] ==2]


    unikalnye = [chislo for chislo in chisla if chastota[chislo] == 1]
    f = True
    for i in unikalnye:
        for j in povtory:
            if j < i:
                f = False

    if f:
        kolvo += 1

print(kolvo)