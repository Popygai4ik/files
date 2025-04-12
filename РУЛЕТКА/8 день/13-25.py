from fnmatch import fnmatch
# c  = []
mini = 0
def y2(n):
    delits = []
    for u in range(1,n + 1):
        if n % u == 0:
            delits.append(u)
    return ((len(delits) % 2) == 0)
for i in range(10**7+1):
    if fnmatch(str(i),'?4*7?') and y2(i):
        mini = i
        break
bol = 0
for i in range(10**7+1, 0, -1):
    if fnmatch(str(i),'?4*7?') and y2(i):
        bol = i
        break
print(bol - mini)
