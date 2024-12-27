from ipaddress import *

ip_net = ip_network('181.165.17.108/255.255.192.0', 0)
c = 0
k = 0
for id in ip_net:
    if f'{id:b}'.count('0') % 9 == 0:
        c += 1
    if f'{int(id):b}'.zfill(32).count('0') % 9 == 0:
        k += 1
print(c, k)