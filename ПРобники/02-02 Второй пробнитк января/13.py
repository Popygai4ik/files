from ipaddress import *
c = 0
i_net = ip_network('201.89.3.12/255.255.128.0', 0)
for id in i_net:
    # print(str(id).split('.'))
    id_s = [bin(int(k))[2:] for k in str(id).split('.')]
    # print(id_s)
    if ((id_s[0].count('1') + id_s[1].count('1') ))<= ((id_s[2].count('1') + id_s[3].count('1'))):

        c += 1
print(c)
