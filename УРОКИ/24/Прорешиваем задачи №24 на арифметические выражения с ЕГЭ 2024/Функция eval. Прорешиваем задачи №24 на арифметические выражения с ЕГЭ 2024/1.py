res = []
for n, s in enumerate(open('1.txt'), 1):
    # print(n)
    try:
        if eval(s):
            res.append([len(s), n])
    except:
        pass

print(sorted(res, reverse=True)[:-3])
