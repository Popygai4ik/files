from  ipaddress import *
c = 0
for mask in range(1, 33):
    i_n = ip_network(f'48.109.66.139/{mask}', 0)
    s = str(i_n).split('/')
    if s[0] == '48.109.64.0':
        c += 1
print(c)