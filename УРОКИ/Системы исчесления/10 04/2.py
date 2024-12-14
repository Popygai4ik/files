# 1 код
# print(oct(19234 + 465123 - 412**4))
x = oct(19234 + 465123 - 412**4)[3:]
c = 0
for s in x:
    if int(s) % 2 != 1:
        c += 1
print(c)
# 2 код
d = 19234 + 465123 - 412**4
cnt = 0
for x in oct(d)[2:]:
    if x in "1357":
        cnt += 1
print(cnt)