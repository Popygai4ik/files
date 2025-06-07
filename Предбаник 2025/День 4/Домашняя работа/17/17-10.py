f = open('17.10.txt')
a = [int(x) for x in f]
res = []
sumi = sum(x for x in a if x < 0)
for i in range(len(a) - 2):
    if (max(a[i:i+3])*min(a[i:i+3])> sumi):
        res.append(sum(a[i:i+3]))
print(len(res),min(res))
s = a

negative = [x for x in s if x < 0]

result = []



for i in range(len(s) - 2):

    if (min(s[i:i + 3]) * max(s[i:i +  3])) > sum(negative):

        result.append(s[i] + s[i + 1] + s[i + 2])


print(len(result), abs(min(result)))