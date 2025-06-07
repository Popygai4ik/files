f = open('24.3.txt')
s = f.readline()
s = s.replace('O',"E")
s = s.replace('I',"E")
s = s.replace('M',"K")
for i in range(100):
    if 'KE'*i in s:
        print(i)