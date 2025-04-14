s = open('24_1.txt').readline()
c = 0
d = ''
for i in range(len(s)):
    for j in range(i + 2, len(s)):
        if s[i] == 'P' and s[i] == s[j]:
            c += 1
print(c)
