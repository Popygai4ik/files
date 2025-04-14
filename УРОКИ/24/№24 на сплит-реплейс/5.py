f = open('24.5.txt')
s = f.readline()
# s = 'ANT'
s = s.replace('ANT','AN NT')
s = s.replace('AN','NT')
for i in range(100):
    if 'NT'*i in s:
        print(i)