# d = 1
# target_diff = 935
# max_natasha = 0
# best_values = ()
#
# for n in range(1, 100):  # разумный диапазон дней
#     for a1 in range(1, 51 - n):  # чтобы Маша в последний день < 50
#         for b1 in range(1, 1000):
#             # Сумма по формуле арифм. прогрессии
#             masha = ((2 * a1 + (n - 1) * d) / 2) * n
#             natasha = ((2 * b1 + (n - 1) * d) / 2) * n
#
#             if (natasha - masha == target_diff) and (natasha % 1 == 0):
#                 # Проверка на пункт а и б
#                 if n in [5, 9]:
#                     print(f"Может быть за {n} дней: Маша={a1}, Наташа={b1}, разница=935")
#                 # Обновляем максимум
#                 if natasha > max_natasha:
#                     max_natasha = int(natasha)
#                     best_values = (n, a1, b1)
#
# print("\nОтвет на пункт (в):", max_natasha)
# print(f"(n = {best_values[0]}, Маша с {best_values[1]}, Наташа с {best_values[2]})")
# d = 1
# for n in range(1,1000):
#     s = ((2 *1 + (n - 1)*d)/2)*n
#     if s % 1 == 0 and (s < 500):
#         print(n)
def sum_arith(a, d, n):
    return (2 * a + (n - 1) * d) * n // 2

# Пункт А
print("а)")
for petya_start in range(1, 100):
    vasya_start = petya_start - 1
    petya_total = sum_arith(petya_start, 2, 5)
    for vasya_days in range(1, 100):
        vasya_total = sum_arith(vasya_start, 1, vasya_days)
        if vasya_total == petya_total:
            print(f"Да, при Петя с {petya_start}, Вася с {vasya_start}, Петя 5 дней, Вася {vasya_days} дней, всего {petya_total} задач")
            break
    else:
        continue
    break

# Пункт Б
print("\nб)")
for petya_start in range(1, 100):
    vasya_start = petya_start + 1
    petya_total = sum_arith(petya_start, 2, 4)
    for vasya_days in range(1, 100):
        vasya_total = sum_arith(vasya_start, 1, vasya_days)
        if vasya_total == petya_total:
            print(f"Да, при Петя с {petya_start}, Вася с {vasya_start}, Петя 4 дня, Вася {vasya_days} дней, всего {petya_total} задач")
            break
    else:
        continue
    break

# Пункт В
def sum_arith(a, d, n):
    return (2 * a + (n - 1) * d) * n // 2

print("в)\nИщем минимальное общее число задач при условии, что оба решают больше 6 дней и один начал на 1 задачу больше...")

min_total = float('inf')
best = None

for petya_days in range(7, 100):
    for vasya_days in range(7, 100):
        for diff in [-1, 1]:  # разница между первым днем Васи и Пети
            for base in range(1, 100):
                p_start = base
                v_start = base + diff
                petya_total = sum_arith(p_start, 2, petya_days)
                vasya_total = sum_arith(v_start, 1, vasya_days)

                if petya_total == vasya_total and petya_total < min_total:
                    min_total = petya_total
                    best = {
                        'petya_start': p_start,
                        'petya_days': petya_days,
                        'vasya_start': v_start,
                        'vasya_days': vasya_days,
                        'total': petya_total
                    }

# Вывод ответа
print(f"\nНаименьшее общее количество задач: {best['total']}")
print(f"Петя: {best['petya_days']} дней, начинал с {best['petya_start']} задач")
print("Прогрессия Пети:", [best['petya_start'] + 2 * i for i in range(best['petya_days'])])
print(f"Вася: {best['vasya_days']} дней, начинал с {best['vasya_start']} задач")
print("Прогрессия Васи:", [best['vasya_start'] + i for i in range(best['vasya_days'])])
