f = open('test.txt')
c = 0
for i in f:
    s = i.split()
    s.sort()
    med = sum(s[1:3])/2
    if len(set(s)) == 3 and int(s[0])+int(s[-1]) > med:
        c += 1
print(c)
cnt = []

for s in f:

    nums = sorted(map(int, s.split()))

    if len(set(nums)) == 3 and nums[0] + nums[-1] > sum(nums[1:3])/2:

        cnt.append(nums)

print(len(cnt))