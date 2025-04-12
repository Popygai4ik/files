from itertools import *
c = 0
for i in product('ГАРОПЕ', repeat=6):
    w = ''.join(i)
    if len(set(w)) < 4:
        continue

    if 'А' not in w[1:5]:
        continue
    if any(w.count(j) > 2 for j in set(w)):
        continue
    s = w
    for k in 'ГРП':
        s = s.replace(k,'S')
    if 'SА'  in s or 'АS'  in s:
        continue
    c+= 1
    print(w)
    # if len(set(w)) >= 4 and w.count("А") >= 1 and (w.index('А') in [1,2,3,4]):
    #     kol = []
    #     for j in set(w):
    #         kol.append(w.count(j))
    #     if not(kol.count(1) >= 2):
    #         s = w
    #         for k in 'ГРП':
    #             s = s.replace(k,'S')
    #         if 'SА' not in s and 'АS' not in s:
    #                 c += 1



print(c)
