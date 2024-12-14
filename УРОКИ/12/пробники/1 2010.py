s = 97 * '5' + '2'
while '555' in s or '52' in s:
    if int(s[-1]) % 2 ==0:
        if '52' in s:
            s = s.replace('52', '5')
    else:
        if '555' in s:
            s = s.replace('555', '52')
        else:
            break

c = 0
for i in s:
    if int(i) % 2 == 0:
        c += 1
print(c)