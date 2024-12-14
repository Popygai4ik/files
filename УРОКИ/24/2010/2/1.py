f= open('24.1.txt')
s= f.readline()
s = s.replace('A', "+")
s = s.replace('B', "+")
s = s.replace('C', "+")
while '++' in s:
    s = s.replace('++', '+ +')
ans = s.split()
print(len(max(ans, key=len)))
