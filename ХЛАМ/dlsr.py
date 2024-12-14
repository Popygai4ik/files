"""
2 По заданным IP-адресу узла сети и маске определите адрес сети: IP-адрес: 10.8.248.131 Маска: 255.255.224.0
"""
# from ipaddress import *
# net = ip_network('10.8.248.131/255.255.224.0',0)
# for ip in net:
#     print(ip)
#     break
"""
3 Для узла с IP-адресом 92.52.42.52 адрес сети равен 92.52.42.0. Чему равно наибольшее возможное значение последнего (самого правого) байта маски?
"""
# from ipaddress import *
# for i in range(31,-1,-1):
#     net1 = ip_network("92.52.42.52/"+ str(i),0)
#     net2 = ip_network("92.52.42.0/"+ str(i),0)
#     sub1 = str(net1).split("/")
#     sub2 = str(net2).split("/")
#     if sub1[0] == sub2[0]:# 􀉨􀉞􀉧􀉚 􀉫􀉟􀉬􀉶
#         print(net1.netmask)
#         break
"""
4 Сеть задана IP-адресом 135.221.128.0 и маской сети 255.255.128.0. Определите минимальную сумму единиц в двоичной записи IP-адреса в этой сети.
"""
# from ipaddress import *
# res = []
# network = ip_network(f'135.221.128.0/255.255.128.0')
# for ip in network:
#     res.append( f'{ip:b}'.kilvo('1') )
# print(min(res))
"""
5. Сеть задана IP-адресом 154. 233.0.0 и маской сети 255.255.0.0. Сколько в этой сети IP-адресов, двоичная запись которых оканчивается на 0?

"""
# from ipaddress import *
# k = 0
# network = ip_network(f'154.233.0.0/255.255.0.0')
# for ip in network:
#    if f'{ip:b}'[-1] == '0':
#         k += 1
# print(k)
"""
6. Сеть задана IP-адресом 143.198.224.0 и маской сети 255.255.240.0. Сколько в этой сети IP-адресов, у которых количество нулей в двоичной записи IP-адреса нечётно?

"""
from ipaddress import *
k = 0
network = ip_network(f'172.16.192.0/255.255.192.0')
for ip in network:
   if f'{ip:b}'.count('1') % 2 == 0:
        k += 1
print(k)
"""
7 Для узла с IP-адресом 193.22.209.132 адрес сети равен 193.22.209.128. Каково наименьшее возможное количество нулей в двоичной записи маски?
"""
# from ipaddress import *
# ip = ip_address('193.22.209.132')
# net = ip_address('193.22.209.128')
# for mask in range(33):
#    network = ip_network(f'{ip}/{mask}', 0)
#    if network.network_address == net:
#        print(32 - mask)
"""
8. Для узла с IP-адресом 151.168.147.193 адрес сети равен 151.168.147.128. Каково наибольшее возможное количество единиц в двоичной записи маски?
"""
# from ipaddress import *
# ip = ip_address('151.168.147.193')
# net = ip_address('151.168.147.128')
# for mask in range(33):
#    network = ip_network(f'{ip}/{mask}', 0)
#    if network.network_address == net:
#        print(mask)
"""
9. Сеть, в которой содержится узел с IP-адресом 159.242.A.223, задана маской сети 255.255.254.0, где А - некоторое допустимое для записи IP
-адреса число. Определите максимальное значение А, для которого для всех IP-адресов этой сети в двоичной записи IP-адреса суммарное количество н
улей в левых двух байтах меньше суммарного количества нулей в правых двух байтах.
"""
# from ipaddress import *
# mask = ip_address('255.255.254.0')
# for A in range(256):
#    ip = ip_address(f'159.242.{A}.223')
#    network = ip_network(f'{ip}/{mask}', 0)
#    if ip not in [network.network_address, network.broadcast_address]:
#        if all( f'{ip:b}'[:16].kilvo('0') < f'{ip:b}'[16:].kilvo('0')
#            for ip in network):
#            print(A)

