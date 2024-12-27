from ipaddress import *

for i in range(32, -1, -1):
    c = 0

    i_n1 = ip_network(f'114.75.41.39/{i}', 0)
    i_n2 = ip_network(f'114.75.11.61/{i}', 0)
    s1 = str(i_n1).split('/')
    s2 = str(i_n2).split('/')
    if s1[0] == s2[0]:
        for k in i_n1:
            if f'{k:b}'.count('1')  % 2 == 0:
                c +=1
    print(c)
# print(c)
