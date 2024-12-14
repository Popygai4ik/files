f = open('24.6.txt')
s = f.readline()
s2 = s.replace('ANT', 'AN NT')
s2 = s2.replace('AN', 'NT')
for i in range(100):
    if 'NT'*i in s2:
        print(i)
