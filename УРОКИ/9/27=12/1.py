f = open('1.txt')
c = 0
for s in f:
    a = list(map(int, s.split()))
    # print(a)
    s1 = (max(a) + min(a)) * 3
    s2 = 2 * (sum(a) - max(a) - min(a))
    if len(set(a)) == 5 and s1 >= s2:
        c += 1
print(c)