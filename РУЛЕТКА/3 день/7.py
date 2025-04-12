from ipaddress import *
c = 0
i_n = ip_network('231.174.192.98/255.255.0.0', 0)
for id in i_n:
    iders = str(id).split('.')
    iders_bin = [bin(int(j))[2:].zfill(8) for j in iders]
    r = ''.join(iders_bin)
    if r.count('1') % 2 == 0:
        c += 1


print(c)
