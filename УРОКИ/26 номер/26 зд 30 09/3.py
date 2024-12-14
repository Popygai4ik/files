f = open("26.3 (1).txt")
# f = open('t.txt')
n = map(int, f.readline().split())
boxes = []
for stroka in f:
    dlina, sivet = stroka.split()
    boxes.append([int(dlina), sivet])
boxes.sort(reverse=True)
bloki = []
while len(boxes) != 0:
    gift = [boxes[0]]
    del boxes[0]
    for i in boxes[:]:
        if gift[-1][0] - i[0] >= 8 and gift[-1][1] != i[1]:
            gift.append(i)
            boxes.remove(i)
    bloki.append(gift)
print(len(max(bloki, key=len)), len(bloki))
