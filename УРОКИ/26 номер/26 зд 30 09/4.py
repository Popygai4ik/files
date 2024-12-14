# f = open("26_skoro_ege.txt")
f = open('t.txt')
n = map(int, f.readline().split())
boxes = []
for stroka in f:
    dlina, sivet = stroka.split()
    boxes.append([int(dlina), sivet])
boxes.sort(reverse=False)
bloki = []
dlina_podar = []
rzmiri_minimal = []
while len(boxes) != 0:
    gift = [boxes[0]]
    del boxes[0]
    for i in boxes[:]:
        if gift[-1][0] - i[0] >= 11 and gift[-1][1] != i[1]:
            gift.append(i)
            boxes.remove(i)
    dlina_podar.append(len(gift))
    rzmiri_minimal.append(gift[-1][0])
    bloki.append(gift)
print(max(dlina_podar), min(rzmiri_minimal))
