f = open('24_4І.txt')
s = f.readline()
s = s.replace('ZXY','*')
s = s.replace('ZYX', '*')
for i in range(1,100):
    if '*' * i in s:
        print(i)