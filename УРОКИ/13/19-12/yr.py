# from ipaddress import *
# for x in range(2, 32):
#     ipnet = ip_network('156.211.113.106/'+str(x), 0)
#     s1 = str(ipnet).split('/')
#     # print(s1)
#     if s1[0] == '156.211.112.0':
#         print(ipnet.netmask)
#         print(s1[1])
from ipaddress import *

ip_net = ip_network('252.67.33.87/255.255.0.0', 0)
c = 0
for id in ip_net:
    s = str(id).split('.')
    if (bin(int(s[0]))[2:].count('1') +  bin(int(s[1]))[2:].count('1') ) < (bin(int(s[2]))[2:].count('1') +  bin(int(s[3]))[2:].count('1') ):
        print(id)
        c +=1
print(c)