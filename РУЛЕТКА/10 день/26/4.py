f = open('56bc761b-7ac0-45d5-afff-ecef54c3fd45_26_155.txt')
# f = open('t')
from collections import defaultdict
n = f.readline()
marki = defaultdict(int)
for s in f:
    mark, su_shtrf, kod = map(int,s.split())
    marki[(mark,kod)] += su_shtrf
max_sum = max(marki.values())
print(max_sum)
takoige = []
for (mark, clas), total in marki.items():
    if total == max_sum:
        takoige.append((mark,clas))
print(takoige)
res_marf, res_cls = max(takoige)
print(res_marf, max_sum)