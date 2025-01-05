a = [int(s) for s in open('5.txt')]
mini = min([x for x in a if abs(x) % 1000 == 600], default=None)

if mini is None:
    print("Нет чисел, оканчивающихся на 600.")
else:
    res = []
    for i in range(len(a) - 2):
        countfivedigit = sum(1 for x in (a[i], a[i + 1], a[i + 2]) if 10000 <= abs(x) < 100000)
        if countfivedigit <= 2 and (a[i] + a[i + 1] + a[i + 2]) >= mini:
            res.append(a[i] + a[i + 1] + a[i + 2])

    if res:
        print(len(res), min(res))
    else:
        print(0)