f = open('26.1.txt')
# f = open('t.txt')
n = int(f.readline())
baxes = [int(i) for i in f]
gifts = []
baxes.sort(reverse=True)
for box in baxes:
    if len(gifts) == 0:
        gifts.append(box)

    elif gifts[-1] - box >= 5:
        gifts.append(box)
    print(gifts[-1])
print(len(gifts), gifts[-1])