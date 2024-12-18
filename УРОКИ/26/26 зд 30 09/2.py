f = open("26,02.txt")
# f = open('t.txt')
Kolvo_korob, Kolvo_lent = map(int, f.readline().split())
boxes = []
lenti = []
for i in range(Kolvo_lent):
    box, lenta = map(int, f.readline().split())
    boxes.append(box)
    lenti.append(lenta)
for i in range(Kolvo_korob - Kolvo_lent):
    box = int(f.readline())
    boxes.append(box)
boxes.sort(reverse=True)
# gift = [boxes[0]]
# for i in boxes[1:]:
#
gift = []
for i in boxes:
    if len(gift) == 0 and i in lenti:
        gift.append(i)
    elif i in lenti and gift[-1] - i >= 7:
        gift.append(i)
razn = max(gift) - min(gift)
print(len(gift), razn)