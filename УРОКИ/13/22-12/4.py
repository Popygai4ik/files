from ipaddress import *

for mask in range(1, 33):
    i_n = ip_network(f'162.14.9.241/{mask}', 0)
    s = str(i_n).split('/')
    if s[0] == '162.14.0.0':
        print(i_n.netmask)
        print(32 - int(s[1]))