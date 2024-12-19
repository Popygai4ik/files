from ipaddress import *

c = 0
for a in range(0, 256):
    i_n = ip_network(f'207.0.{a}.163/255.255.255.192', 0)
    for id in i_n:
        print(f'{id:b}'[:16])
        if (f'{id:b}'[:16].count('0') > f'{id:b}'[16:].count('0') ) == False:
            break
    else:
        c += 1
print(c)