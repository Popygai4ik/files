f = open('2')
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
print(a)
res = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        # print(a[i], a[j], ((a[i] % 2) != 0 )and ((a[j] % 2) != 0) and ((a[i]+a[j]) // 2 in a), (a[i]+a[j]) // 2)
        #
        # if ((a[i] % 2) != 0 )and ((a[j] % 2) != 0) and (biner(a, ((a[i]+ a[j]) // 2)) ):
        #     res.append(((a[i] + a[j]) // 2))
        if ((a[i] % 2) != 0 )and ((a[j] % 2) != 0) and ((a[i]+ a[j]) // 2) in a :
            res.append(((a[i] + a[j]) // 2))

print(len(res),max(res))
# print(res)