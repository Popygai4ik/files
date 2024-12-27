from  ipaddress import  *
i_n = ip_network('141.14.138.235/255.255.224.0', 0)
c = 0
for id in i_n:
    s = str(id).split('.')
    # print(s)
    if s[0] != '141':
        continue

    if str(int(s[-1]) % 10) not in '02468':
        continue
    f= True
    for f in s:
        if  int(f) > 200:
            f = False
    if not f:
        continue
    c += 1
    print(id)
print(c)
