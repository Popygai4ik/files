from ipaddress import *

i_n = ip_network('192.168.32.160/255.255.255.240', 0)
c  = 0
for ad in i_n:
    if f'{ad:b}'.count('1') % 2 != 0:
        c += 1
print(c)
