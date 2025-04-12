a = [int(s) for s in open('d9355f96-4337-48b6-9bcf-a03a4b21c534_17_1 (1).txt')]
def pr(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for d in range(3, int(x**0.5)+1, 2):
        if x % d == 0:
            return False
    return True
maxi = max(i for i in a if str(i)[-2:] == '33')
print(maxi)
res = []
for i in range(len(a) - 1):
    n1 = a[i]
    n2 = a[i+1]
    y1 = (((pr(n1))+(pr(n2))) == 1)
    y2 = ((abs(n1+n2)) % maxi == 0)

    if y2 and y1:
        print(y1, y2, n1,n2)

        res.append(n1*n2)
if res:
        print(len(res), max(res))
else:
    print("✅ Условию соответствующих пар не найдено.")

