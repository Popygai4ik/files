print('a b c d f')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                f= ((not(c <= b)) and (d <= a) != (b and c and d and (not(a))))
                if f == 1:
                    print(a,b,c,d,f)