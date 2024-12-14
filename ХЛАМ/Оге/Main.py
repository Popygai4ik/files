# 4
# from ipaddress import *
# net = ip_network("192.168.156.235/255.255.255.240",0)
# k = 0
# for ip in net.hosts():
#     k += 1
#     if ip == ip_address("192.168.156.235"):
#         print(k)
#         break
# 5
# from ipaddress import *
# for i in range(32):
#     net = ip_network("248.228.60.240/"+ str(i),0)
#     sub = str(net).split("/")
#     if sub[0] == "248.228.56.0":
#         print(net.netmask)
# 6
# from ipaddress import *
# for i in range(31,-1,-1):
#     net1 = ip_network("121.171.15.70/"+ str(i),0)
#     net2 = ip_network("121.171.3.68/"+ str(i),0)
#     sub1 = str(net1).split("/")
#     sub2 = str(net2).split("/")
#     if sub1[0] == sub2[0]:
#         print(net1.netmask)
#         break
# 7
# from ipaddress import *
# k = 0
# for i in range(32):
#     net = ip_network("148.195.140.28/"+ str(i),0)
#     sub = str(net).split("/")
#     if sub[0] == '148.195.140.0':
#         k += 1
# # print(k)
from ipaddress import*
# k = []
# IP1 = ip_address('121.171.15.149')
# IP2 = ip_address('121.171.15.143')
# for x in range(24,32):
#     for y in range(256):
#         net = ip_network('121.171.15.'+str(y)+'/'+str(x),0)
#         if IP1 in net and IP2 in net:
#             k.append(net.num_addresses)
# print(min(k))
net = ip_network("162.198.75.44/255.255.240.0",0)
k = 0
for ip in net.hosts():
    k +=1
    if ip == ip_address("162.198.75.44"):
        print(k)
        break