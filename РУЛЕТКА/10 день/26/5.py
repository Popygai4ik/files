# Читаем данные из файла
with open("753b4f26-6dea-437b-ad5f-9d3096422638_26_new.txt") as f:
    n = int(f.readline())
    data = []

    for line in f:
        parts = list(map(int, line.split()))
        ID = parts[0]
        answers = parts[1:]

        # Вычисляем 3 критерия:
        total = sum(answers)
        positive = sum(x for x in answers if x > 0)
        answered = sum(1 for x in answers if x != 0)

        # Добавляем участника: (сумма, плюсы, ответы, ID)
        data.append((total, positive, answered, ID))

# Сортировка по убыванию суммы, плюсов, ответов, по возрастанию ID
data.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))

# Рассчитаем размер первой трети
third = n // 3 + (1 if n % 3 != 0 else 0)

# Пороговые значения последнего участника, прошедшего в тур
last_passing = data[third - 1][:3]  # только сумма, плюсы, ответы

# Находим первого, кто не прошел
first_not_passing_id = None
for participant in data[third:]:
    if participant[:3] != last_passing:
        first_not_passing_id = participant[3]
        break

# Найдём участника на 2300-м месте
target_metrics = data[2299][:3]  # сумма, плюсы, ответы

# Считаем, сколько человек имеют те же показатели
count_same_as_2300 = sum(1 for p in data if p[:3] == target_metrics)

# Выводим ответ
print(first_not_passing_id, count_same_as_2300)
