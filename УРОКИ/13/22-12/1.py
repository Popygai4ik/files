from ipaddress import *


c= 0
ip_net = ip_network('181.165.17.108/255.255.192.0', 0)
for id in ip_net:
    if f'{int(id):b}'.count('1') % 2 != 0:
        c += 1
print(c)