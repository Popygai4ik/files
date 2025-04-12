f = open('24-12')
s = f.readline()
arf = ''
max_zn = 0
for i in range(len(s)):
    # print(arf)
    if s[i] in '345':
        arf += s[i]
        max_zn = max(max_zn, eval(arf))
    elif s[i] in '-*' and len(arf) > 0 and arf[-1] not in '-*':
        arf += s[i]
    elif s[i] == '0' and len(arf) > 0 and arf[-1] not in '-*':
        arf += s[i]
        max_zn = max(max_zn, eval(arf))
    else:
        arf = ''
print(max_zn)
