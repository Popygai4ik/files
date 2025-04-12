def min_curators(N, start, end, times):
    # Сортируем кураторов по времени начала работы
    times.sort(key=lambda x: x[0])  # Сортируем по времени начала

    curators = []  # Список для хранения выбранных кураторов
    current_time = start  # Начинаем с момента начала экзамена
    first_curator_time = None  # Время первого куратора

    while current_time < end:
        best_curator = None
        for a, b in times:
            # Находим куратора, который может покрыть текущий момент времени
            if a <= current_time < b:
                if not best_curator or b > best_curator[1]:
                    best_curator = (a, b)

        if not best_curator:
            break  # Если нет подходящего куратора, выходим

        # Добавляем куратора в список
        curators.append(best_curator)
        current_time = best_curator[1]  # Обновляем текущее время

        # Запоминаем время начала работы первого куратора (когда он начинает после start)
        if first_curator_time is None:
            first_curator_time = best_curator[0] - start

    return len(curators), first_curator_time

# Входные данные
with open('е') as f:
    N, start, end = map(int, f.readline().split())  # Преобразуем start, end и N в целые числа
    times = [tuple(map(int, line.split())) for line in f]  # Преобразуем интервалы в кортежи чисел

# Вызов функции
result = min_curators(N, start, end, times)
print(result[0], result[1])
