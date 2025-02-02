s = '3'*11 + 19*'4'
while '4444' in s or '333' in s:
    while '4444' in s:
        s = s.replace('4444', '3', 1)
    while '333' in s:
        s = s.replace('333', '4', 1)
print(s)
