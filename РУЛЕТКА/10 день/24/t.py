

with open("24_1.txt") as f:
    s = f.read().strip()

count = 0

for i in range(len(s)):
    for j in range(i + 2, len(s)):
        if s[i] == s[j]:
            count += 1

print(count)
