f = open("1.txt")

cnt = 0

for s in f:

    a = list(map(int, s.split()))

    if a[2] - a[1] == a[1] - a[0]:

        cnt += 1

print(cnt)