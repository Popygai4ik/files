f = open('1')
n = int(f.readline())
def biner(a, sh):
    lef = 0
    rir = len(a) -1
    while lef <= rir:
        md = (lef + rir) // 2
        if a[md] == sh:
            return True
        elif a[md] < sh:
            lef = md + 1
        else:
            rir = md - 1
a = [int(s) for s in f]
a.sort()
res = []
for i in range(n):
    for j in range(i + 1, n):
        # print(a[i], a[j])
        if (((a[i] % 2 == 0) + (a[j] % 2 == 0)) == 1 and ((biner(a, a[i] + a[j])))):
            res.append(a[i]+a[j])
print(len(res), max(res))