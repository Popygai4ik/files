f = open("24.5.txt")
s = f.readline()
# s.replace('AN', 'NT')
s.replace('NT', 'AN')
for i in range(100):
    if 'AN' *i  in s:
        print(i)