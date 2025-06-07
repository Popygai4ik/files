f = open('24_2.txt')
s = f.readline()
a = s.split('Y')
print(len(max(a,key=len)))