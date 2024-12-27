from ipaddress import *
c = 0
i_n = ip_network('176.54.23.0/255.255.224.0', 0)
for i in i_n:
    if str(i).count('2') % 3 == 0:
        c += 1
print(c)