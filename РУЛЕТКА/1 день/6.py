from ipaddress import *
c = 0
i_n = ip_network('213.232.128.145/255.255.128.0',0)
for id in i_n:
    a = (list(i for i in str(id).split('.')))
    a2 = []
    for i in a:
        s = bin(int(i))[2:]
        while len(s) < 8:
            s = '0' + s
        a2.append(s)
    # a3 = [len(i) for i in a2]
    # print(a3)
    s = ''.join(a2)
    if s.count('0') % 5 == 0:
        c += 1
print(c)
