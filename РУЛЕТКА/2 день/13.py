def M(n):
    delet = []
    for x in range(2,n):
        if n % x == 0:
            if len(delet) < 5:
                delet.append(x)
            else:
                break
    if len(delet) == 5:
        k = 1
        for el in delet:
            k = k * el
        return k
    else: return 0
for sh in range(400000010, 400000011):
    if 0 < M(sh)< sh:
        print(M(sh))
    else:
        continue
# 400000010
