# 12 - 64
# 13 - 109
# for n in range(1,1000):
#     bib = bin(n)[2:]
#     if sum(map(int,bib)) % 2 == 0:
#         bib = bib + "0"
#         bib = '100' + bib[3:]
#     else:
#         bib = bib + "1"
#         bib = '111' + bib[3:]
#     R = int(bib,2)
#     # print(n,R)
#     if R > 128:
#         print(n)
#         break
# res = []
# for n in range(1,1000):
#     bib = bin(n)[2:]
#     if n % 2 == 0:
#         bib = '10' + bib
#     else:
#         bib = '1' + bib +'01'
#     R= int(bib,2)
#     # print(n,R)
#     if n <= 12:
#         res.append(R)
# print(max(res))
# for n in range(1,1000,2):
#     bib = bin(n)[2:]
#     bib2 = bib[1:-1].replace('1', '2')
#
#     bib2 = bib2.replace('0', "1")
#     bib2 = bib2.replace('2', '0')
#     bib = bin(n)[2:][0] + bib2 + bin(n)[2:][-1]
#     R = int(bib,2) + n
#     if R > 300:
#         print(n)

# n = 6
# bib = bin(n)[2:]
# nach = bib[0]
# kon = bib[-1]
# bib2 = bib[1:-1].replace('1', '2')
#
# bib2 = bib[1:-1].replace('0', "1")
# bib2 = bib[1:-1].replace('2', '0')
# bib = nach + bib2+kon
# print(int(bib, 2) + n)

# 17 - 23

# def to_5(n):
#     res= ''
#     while n> 0:
#         res += str(n % 5)
#         n = n // 5
#     return res[::-1]
#
# for n in range(1,1000):
#     biib = to_5(n)
#     if n % 10 == 0:
#         biib += biib[-2:]
#     else:
#         biib = to_5((n % 10 ) * 3) + biib
#     R= int(biib,5)
#     if R < 281:
#         print(n)
# 18 - 248
# 19 - 224
# 20  - 11
# 21  - 1555
# 22 - 1024
# 23 - 3003
from  ipaddress import  *
# for i in range(1,33):
#     i_n = ip_network(f'148.228.124.242/{i}',0)
#     s = str(i_n).split('/')
#     # print(s)
#     if s[0] == '148.228.120.0':
#         print(i_n.netmask)
# for i in range(1,33):
#     ip_net1 = ip_network(f'121.171.31.70/{i}', 0)
#     ip_net2 = ip_network(f'121.171.15.68/{i}', 0)
#     s1 = str(ip_net1).split('/')
#     s2 = str(ip_net2).split('/')
#     if s1[0] == s2[0]:
#         print(ip_net2.netmask)
# for i in range(1,33):
#     ip_net = ip_network(f'192.168.104.15/{i}', 0)
#     s = str(ip_net).split('/')
#     if s[0] == '192.168.104.0':
#         print(32 - i)
# in_net = ip_network('132.126.150.18/255.255.240.0', 0)
# n = 1
# for id in in_net:
#     # print(t(id))
#     if str(id) == '132.126.150.18':
#         print(n)
#     n +=1
# i_n = ip_network('172.16.80.0/255.255.248.0',0)
# c = 0
# for id in i_n:
#     v1 = [bin(int(k))[2:].zfill(8) for k in str(id).split('.')]
#     bib = ''.join(v1)
#     # print(id,''.join(v1),f'{id:b}')
#     if bib.count('1') % 2 != 0:
#         c+= 1
# print(c)
# i_n = ip_network('112.208.0.0/255.255.128.0', 0)
# c = 0
# for id in i_n:
#     v1 = [bin(int(k))[2:].zfill(8) for k in str(id).split('.')]
#     bib = ''.join(v1)
#     if bib.count('1') % 11 == 0:
#         c+=1
# print(c)
# n = 0
# i_n = ip_network('156.128.0.227/255.255.255.248', 0)
# for id in i_n:
#     print(id)
#     if str(id) == '156.128.0.227':
#         print(n)
#     n +=1
# # print(n)
# for i in range(1,33):
#     i_n = ip_network(f'108.133.75.91/{i}', 0)
#     s = str(i_n).split('/')
#     if s[0] == '108.133.75.64':
#         k = 0
#         for i in i_n:
#             k +=1
#         print(k)
# i_n = ip_network('11.92.135.56/255.224.0.0',0)
# for id in i_n.hosts():
#     print(id)
# i_n = ip_network('98.81.154.195/255.252.0.0',0)
# for id in i_n.hosts():
#     print(id)
# i_n = ip_network('252.67.33.87/255.255.0.0',0)
# c= 0
# for id  in i_n:
#     v1 = [bin((int(k)))[2:].zfill(8) for k in str(id).split('.')]
#     # print(v1)
#     lev= v1[0] + v1[1]
#     prav = v1[2] + v1[3]
#     if prav.count('1')>lev.count('1'):
#         c += 1
# print(c)
for i in range(0,256):
    try:
        # print(f'199.59.129.3/255.255.{i}.0')
        i_n = ip_network(f'199.59.129.3/255.255.{i}.0', 0)
        # print(i)
        for id in i_n.hosts():
            # print(id)
            v1 = [bin((int(k)))[2:].zfill(8) for k in str(id).split('.')]
                # print(v1)
            lev= f'{id:b}'[:16]
            prav = f'{id:b}'[16:]
            if (lev.count('1') >= prav.count('1')) == False:
                # print(1)
                break

        else:
            print(i_n.netmask)
    except:
        pass
