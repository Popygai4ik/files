f = open('17.11.txt')
a = [int(x) for x in f]
res = []

# maxi = max(x for x in a if x % 100 == 11)
for i in range(len(a) - 1):
    chek = [x for x in a[i:i+2] if len(str(x)) == int(str(x)[0])]

    if len(chek) == 2:
        res.append(a[i] + a[i + 1])
print(len(res), min(res))