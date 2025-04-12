with open('t.txt') as f:
    n, k = map(int, f.readline().split())
    parcels = []
    for _ in range(n):
        weight, cost = map(int, f.readline().split())
        parcels.append((weight, cost))

# Сортируем по убыванию "стоимость за кг"
parcels.sort(key=lambda x: x[1] / x[0])

# Берём топ-K посылок
selected = parcels[:k]

# Суммарный вес
total_weight = sum(p[0] for p in selected)

# Стоимость самой тяжёлой посылки среди выбранных
max_weight_cost = max(selected, key=lambda x: x[0])[1]

print(total_weight, max_weight_cost)
