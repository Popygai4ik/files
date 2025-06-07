# for n in range(1,1000):
#     bib = bin(n)[2:]
#     if n % 5 == 0:
#         bib = bib + bib[-3:]
#     else:
#         bib = bib + bin((n % 5) * 4)[2:]
#     R = int(bib,2)
#     if R > 150:
#         print(n)

# for n in range(1,1000):
#     bib = bin(n)[2:]
#     if bib.count('1') % 2 == 0:
#         bib = '10' + bib[2:] + "0"
#     else:
#         bib = '11' + bib[2:] + "11"
#     R= int(bib,2)
#     if R < 99:
#         print(n)

# for n in range(1,1000):
#     bib = bin(n)[2:]
#     if bib.count('1') % 2 == 0:
#         bib = '10'+bib[2:] + '0'
#     else:
#         bib = '11' + bib[2:] + '1'
#     R = int(bib,2)
#     # rint(n,R)p
#     if R < 20:
#         print(n)
# res = []
# for n in range(1,10000):
#     bib = bin(n)[2:]
#     if n % 2 == 0:
#         bib = bib + bib[:2]
#     else:
#         bib = '1' + bib + '0'
#     R = int(bib,2)
#     if R > 7318:
#         res.append(R)
# print(min(res))

# for n in range(1,1000):
#     bib = bin(n)[2:]
#     bib2 = bib[1:-1].replace('1','2')
#     bib2 = bib2.replace('0','1')
#     bib2 = bib2.replace('2', '0')
#     bib = bin(n)[2:][0] + bib2 + bin(n)[2:][-1]
#     r = int(bib,2) + n
#     if  r > 400:
#         print(n)

# res = []
# for  n in range(1,1000):
#     bib = bin(n)[2:]
#     if bib.count('1') % 2 == 0:
#         bib = bib + '0'
#     else:
#         bib = bib + '1'
#     if bib.count('1') % 2 == 0:
#         bib = bib + '0'
#     else:
#         bib = bib + '1'
#
#     r = int(bib,2)
#     if r < 268:
#         res.append(r)
# print(max(res))

def to3(n):
    res = ''
    while n > 0:
        res += str(n % 3)
        n = n // 3
    return res[::-1]
#
# for n in range(1,1000):
#     bib = to3(n)
#     if n % 3 == 0:
#         bib = bib + bib[-3:]
#     else:
#         bib = bib + to3((n % 3) * 3)
#     r = int(bib, 3)
#     if r > 344:
#         print(n)
# for n in range(1,1000):
#     bib = to3(n)
#     if n % 3 == 0:
#         bib = bib + bib[-3:]
#     else:
#         bib = bib + to3((n % 3) * 3)
#     r = int(bib,3)
#     if r > 340:
#         print(n)
#
# def to5(n):
#     res = ''
#     while n > 0:
#         res += str(n % 5)
#         n = n // 5
#     return res[::-1]
#
# for n in range(1,1000):
#     bib = to5(n)
#     if n % 10 == 0:
#         bib = bib + bib[-2:]
#     else:
#         bib = to5((n % 10) * 3) + bib
#     r = int(bib, 5)
#     if r < 176:
#         print(n)
# def to4(n):
#     res = ''
#     while n > 0:
#         res += str(n % 4)
#         n = n // 4
#     return res[::-1]
#
# for n in range(1,10000):
#     bib = to4(n)
#     if n % 3 == 0:
#         bib = bib + bib[-3:]
#     else:
#         bib = to4((n % 3) * 4) + bib
#     r = int(bib,4)
#     if r < 1166:
#         print(n)
from  ipaddress import *
# for i in range(33):
#     i_n = ip_network(f'170.155.137.181/{i}', 0)
#     s = str(i_n).split('/')
#     if s[0] == '170.155.136.0':
#         print(i_n.netmask)
# i_n = ip_network('154.24.17.13/255.255.240.0', 0)
# for i in i_n:
#     print(i,f'{i:b}', f'{i:b}'.count('0'))
# c = 0
# i_n = ip_network('172.16.192.0/255.255.192.0', 0)
# for id in i_n:
#     v1 = [bin(int(k))[2:].zfill(8) for k in str(id).split('.')]
#     bib = ''.join(v1)
#     if bib.count('1') % 2 == 0:
#         c+= 1
# print(c)
# c = 0
# i_n  = ip_network('181.165.17.108/255.255.192.0', 0)
# for id in i_n:
#     if f'{id:b}'.count('0') % 9 == 0:
#         c += 1
# print(c )
# for i in range(33):
#     ip_networ = ip_network(f'203.86.7.230/{i}', 0)
#     s = str(ip_networ).split('/')
#     # print(s[0])
#     if s[0] == '203.86.0.0':
#         print(32 - i)
# i_n = ip_network('196.168.77.128/255.255.255.0', 0)
# for id in i_n.hosts():
#     print(id)
#     break
# i_n = ip_network('97.191.34.206/255.255.255.240',0)
# for id in i_n.hosts():
#     print(id)
# i_n = ip_network('123.168.72.213/255.255.255.224', 0)
# for id in i_n.hosts():
#     print(id)
# i_n = ip_network('242.52.23.67/255.255.128.0', 0)
# c = 0
# for id in i_n:
#     s= f'{id:b}'
#     lev = s[:16]
#     prav = s[16:]
#     if prav.count('1') * 2 < lev.count('1'):
#         c+= 1
# print(c)
# i_n = ip_network('123.123.123.123/255.255.255.128', 0)
# c = 0
# print(f'{i_n.netmask:b}')
# for i in i_n:
#     c+= 1
# print(c-2)
# def prost(n):
#     for x in range(2,n):
#         if n % x == 0:
#             return False
#     return True
#
# for n in range(1000,10000):
#     bib = bin(n)[2:]
#     if prost(sum(list(map(int, str(n))))):
#         bib = bib + bib[-3:]
#     else:
#         bib = bib[::-1] + bin((n % 4)*4)[2:]
#     r = int(bib,2)
#     if len(set(str(n))) >= 3 and r > 100_000 and prost(n):
#         print(n)
