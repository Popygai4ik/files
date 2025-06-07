f = open('24.5.txt')
s = f.readline()
s = s.replace('ANT',"AN NT")
s = s.replace('AN', "NT")
for i in range(1,100):
    if 'NT' * i in s:
        print(i)