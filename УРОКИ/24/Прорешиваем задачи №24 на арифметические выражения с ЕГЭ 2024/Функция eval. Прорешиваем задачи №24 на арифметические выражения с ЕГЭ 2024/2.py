res = []
for n, s  in enumerate(open('2.txt'), start=1):
    try:
        res.append([eval(s), n])
    except:
        pass
print(sorted(res)[-2:])
