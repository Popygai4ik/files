s = 40 * '7'
while '7777' in s or '3333' in s:
    if '3333' in s:
        s = s.replace('3333', '77', 1)
    else:
        s = s.replace('7777', '33', 1)
print(s)