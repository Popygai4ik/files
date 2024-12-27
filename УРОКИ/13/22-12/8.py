from ipaddress import *
from ipaddress import ip_network
c = 0
i_n = ip_network('192.192.192.241/255.255.255.240', 0)
for i in i_n:
    c +=1
print(c)