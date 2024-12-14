c = 0
for N in range(234_567_900, 789_012_346):
    s = '1'*N
    while '111' in s:
        s = s.replace('111', '2')
        s = s.replace('222', '11')
        s = s.replace('1', '2')
    print(len(s))
    if len(s) == 3:
        c+=1
print(c)