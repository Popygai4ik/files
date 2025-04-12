from ipaddress import *
c = 0
i_n = ip_network('174.101.64.62/255.255.240.0', 0)
for id in i_n:
    iders = str(id).split('.')
    iders_bin = [bin(int(j))[2:].zfill(8) for j in iders]
    if (iders_bin[2].count('1')+iders_bin[3].count('1')) % 2 != 0:
        continue
    if (int(iders[2])+int(iders[3]))% 2 == 0:
        continue
    res = []
    print(iders)
    for u in iders:
        res.append((len(set(u))) == len(u))
    if all(res):
        c += 1

print(c)