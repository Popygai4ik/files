f = open('24.3.txt')
s = f.readline()
s = s.replace('E','O')
s = s.replace('I','O')
s = s.replace('M','K')
for i in range(100):
    if 'KO'*i in s:
        print(i)

