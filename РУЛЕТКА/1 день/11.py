a = [int(s) for s in open('11-17')]
res = []
pipo = []
for i in a:
    if i < 0 and i % 29 == 0:
        pipo.append(i)
sh = abs(max(pipo))
for i in range(len(a) - 1):
    if (a[i] != a[i + 1]) and abs(a[i] - a[i + 1]) % sh == 0:
        res.append(a[i] + a[i + 1])
print(len(res),max(res))
res = []

# Находим максимальное отрицательное число, кратное 29
max_neg_29 = max(x for x in a if x < 0 and x % 29 == 0)
sh = abs(max_neg_29)  # Берём модуль

# Перебираем пары
for i in range(len(a) - 1):
    if abs(a[i] - a[i + 1]) % sh == 0:  # Проверяем делимость разности
        res.append(a[i] + a[i + 1])

# Выводим результат без пробелов
print(f"{len(res)}{max(res)}")