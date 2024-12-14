f = open("1.txt")
chipe = []
n, m = map(int, f.readline().split())
# print(n, m)
for s in f:
    rus, inf, mat = map(int, s.split())
    # print(rus,  inf, mat)
    chipe.append([rus, inf, mat, rus+ inf+mat])
chipe.sort(reverse=True, key=lambda x: [x[-1], x[1], x[2]])
print(chipe[:m])
print(chipe[m:m + 10])
# 150