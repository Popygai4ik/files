with open('t') as f:
    stroki = [s.strip() for s in f]
res = []
for i in stroki:
    con = 0
    for k in i:
        if k.isdigit():
            con+=1
    if con >= 20:
        # print(con)
        res.append(i)

# print(len(res))
maxi = 0
for s in res:
    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        indexes = [i for i, c in enumerate(s) if c == ch]
        # print(indexes)
        for i in range(len(indexes)):
            for j in range(i + 1, len(indexes)):
                first = indexes[i]
                last = indexes[j]
                stroka_mexdu = s[first + 1:last]
                if (ch not in stroka_mexdu) and (ch.lower() not in stroka_mexdu):
                    dist = last - first
                    maxi = max(maxi, dist)

print(maxi)
# Process finished with exit code 0
