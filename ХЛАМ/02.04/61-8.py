def perevod_v_shesnatsetiresniu(shislo):
    s = ['0', '1', '2']
    if shislo < 3:
        return s[shislo]
    return perevod_v_shesnatsetiresniu(shislo // 3) + s[shislo % 3]

vod = int(input())
res = perevod_v_shesnatsetiresniu(vod)
res = [i for i in res]
for i in range(len(res)):
    if res[i] == '0':
        res[i] = '-1'
    elif res[i] == '1':
        res[i] = '0'
    elif res[i] == '2':
        res[i] = '1'
for i in res:
    if i != '1':
        print("#", end='')
    else:
        print(i, end='')
