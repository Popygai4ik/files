from ipaddress import *

i_n = ip_network('252.32.33.87/255.255.0.0', 0)
c = 0
k  =0
for id in i_n:
    s=str(id).split('.')
    if ( (bin(int(s[3]))[2:].count('1') + bin(int(s[2]))[2:].count('1')) / (bin(int(s[0]))[2:].count('1') + bin(int(s[1]))[2:].count('1'))) > 2:
        c +=1
    if (f'{id:b}'[16:].count('1') / f'{id:b}'[:16].count('1')) > 2:
        k += 1
print(c)
print(k)