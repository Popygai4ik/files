from ipaddress import *

ip_net = ip_network('142.96.56.118/255.255.255.240', 0)
c = 0
for id in ip_net:
    s = str(id).split('.')
    if (bin(int(s[0]))[2:].count('1') + bin(int(s[1]))[2:].count('1')) < (bin(int(s[3]))[2:].count('1') + bin(int(s[2]))[2:].count('1')):
        c += 1
print(c)