from ipaddress import *
# for i in range(1, 33):
#     ip_net = ip_network(f'192.168.104.15/{i}', 0)
#
#     s = str(ip_net).split('/')
#     # print(s)
#     if s[0] == '192.168.104.0':
#         print(32 - int(s[1]))
ip_net = ip_network('192.192.255.225/255.255.254.0', 0)
c = 0
for id in ip_net:
    c += 1
print(c)
print(bin(254))