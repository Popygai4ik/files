from ipaddress import *

for i in range(32):
    i_n = ip_network(f'202.212.201.183/{i}', 0)
    s = str(i_n).split('/')
    print(s)
    if s[0] == '202.212.192.0':
        print(s[1])