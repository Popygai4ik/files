a = [int(i) for i in open('17.txt')]
# c2 = 0
# c1 = 0
res = []
for i in range(len(a) - 2):
    if (a[i] < 0) + (a[i + 1] < 0) + (a[i + 2] < 0) >= 1:
        # c1+= 1
        res.append(sum(a[i:i+3]))
        # print(a[i:i+3])
    # if ((a[i] < 0) or (a[i + 1] < 0) or (a[i + 2] < 0)) == True:
    #     c2 +=1
# print(c1, c2)
print(len(res), min(res))