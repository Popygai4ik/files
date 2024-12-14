f = open("26.1 (1).txt")
# f = open("t.txt")
n = int(f.readline())
boxes = [int(s) for s in f]
boxes.sort(reverse=True)
gift = [boxes[0]]
for i in boxes[1:]:
    if gift[-1] - i >= 5:
        gift.append(i)
print(len(gift), min(gift))