from ipaddress import *
c = 0
i_n = ip_network('201.79.33.112/255.255.192.0', 0)
for id in i_n:
    a1 = [bin(int(i))[2:] for i in str(id).split('.')]
    lef = ''.join(a1[:2])
    pr = ''.join(a1[2:])
    # print(a1)
    # print(lef, pr)
    if lef.count('1') < pr.count('1'):
        c += 1
print(c)
