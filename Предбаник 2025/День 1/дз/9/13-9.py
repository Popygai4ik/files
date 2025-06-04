f = open('23bfc134-3e4d-45c9-8a9c-93eae7402c24_9-12.csv')
c = 0
for s in f:
    a = list(map(int, s.split(',')))
    chet = [i for i in a if i % 2 == 0]
    ne_chet = [i for i in a if i % 2 != 0]
    if len(chet) == 0:
        max_c = 0
    else:
        max_c = max(chet)
    print(ne_chet)
    if len(ne_chet) == 1 or len(ne_chet) == 0 :
        v_max = 0
    else:
        v_max = sorted(ne_chet,reverse=True)[1]
    if len(chet) == 0:
        mix_nc = 0
    else:
        mix_nc = min(chet)
    if (abs(max_c - (sum(a)/len(a)))) > (abs(v_max - mix_nc)):
        c+=1
print(c)