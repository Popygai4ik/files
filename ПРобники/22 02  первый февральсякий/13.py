import ipaddress

for i in range(2, 33):
    i_n = ipaddress.ip_network(f'171.149.165.202/{i}', 0)
    s1 = str(i_n).split('/')
    if s1[0] == '171.149.160.0':
        print(s1)