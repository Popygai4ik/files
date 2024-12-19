from ipaddress import *

for n in range(9):
    a = int('1'*n + '0'*(8 - n), 2)
    i_n = ip_network(f'255.201.33.160/255.255.{a}.0', 0)
    for id in i_n:
        if (f'{id:b}'[:16].count('1')>= f'{id:b}'[16:].count('1')) ==False:
            break
    else:
        print(id)
        print(a)