a = [int(i) for i in open('11')]
res = []
def sustifr(sh):
    res = 0
    for i in str(sh):
        res+= int(i)
    return res
for i in range(len(a) -1 ):
    if len(str(a[i])) == int(str(a[i])[0]) and len(str(a[i + 1])) == int(str(a[i +1 ])[0]):
        # print(a[i], a[i + 1])
        res.append(a[i] + a[i+1])
print(len(res),min(res))