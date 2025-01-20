import re
f = open('3.txt')
res = 0
for s in f:
    pod = re.findall(r"\d+(?:[-+*]\d+)*", s)
    if pod:
        res += 1
print(res)