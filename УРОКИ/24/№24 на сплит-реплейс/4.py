f = open('24_4_.txt')
s = f.readline()
s = s.replace('ZXY', 'ZYX')
# s = s.replace('ZYX', '*')
for i in range(100):
    if 'ZYX'*i in s:
        print(i)