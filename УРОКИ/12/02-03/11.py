s = '9'*130
while '666' in s or '999' in s:
    if '666' in s:
        s = s.replace('666','99', 1)
    else:

        s = s.replace('999','66', 1)
print(s)#9996666699