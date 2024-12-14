kolvo_max, kol_shoto_kypite = [int(input()) for h in range(2)]
if kolvo_max > kol_shoto_kypite:
    kolvo_max = kol_shoto_kypite
d = 0
R = kolvo_max + 2
while R - d > 1:
    mid = (d + R) // 2
    if (mid + kolvo_max) * (kolvo_max - mid + 1) // 2 >= kol_shoto_kypite:
        d = mid
    else:
        R = mid
if (d + kolvo_max) * (kolvo_max - d + 1) // 2 < kol_shoto_kypite:
    print(0)
else:
    for i in range(R, kolvo_max + 1):
        print(i // 2)
    s = (R + kolvo_max) * (kolvo_max - R + 1) // 4
    if kol_shoto_kypite - s > 0:
        print(kol_shoto_kypite - s)
