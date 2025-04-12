f = open('502faff6-3c15-4877-917b-b60149c70337_26.91.txt')
n = int(f.readline())
data = []

for _ in range(n):
    ushast = f.readline().split()
    uid = int(ushast[0])
    scores = list(map(int, ushast[1:]))

    total = sum(scores)
    bolse0 = sum(x for x in scores if x > 0)
    count_soxtexen = sum(1 for x in scores if x != 0)

    data.append((uid, total, bolse0, count_soxtexen))

sorted_data = sorted(data, key=lambda x: (-x[1], -x[2], -x[3], x[0]))


PASS= 333333
poluprohod = sorted_data[PASS - 1][1:]  # (total, positive, count)
print(poluprohod)
first_loser_uid = 0
for i in range(PASS, len(sorted_data)):
    if sorted_data[i][1:] != poluprohod:
        first_loser_id = sorted_data[i][0]
        break

ball_1500 = sorted_data[1499][1:]


cop_ball = sum(1 for item in sorted_data if item[1:] == ball_1500)

print(f"{first_loser_id} {cop_ball}")
# 168 591
