from  ipaddress import *

for i in range(1, 33):
    i_n = ip_network(f'156.211.64.98/{i}', 0)
    s = str(i_n).split('/')
    if s[0] == '156.211.64.0':
        print(i_n.netmask)
        print(i)