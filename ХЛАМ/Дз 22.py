# 2
"""
c = []
for i in range(0, 1000):
    bina = bin(i)
    srt = str(bina)
    s_bina = [int(digit) for digit in str(bina[2:])]
    smu = sum(s_bina)

    if smu % 2 == 0:
        s_bina.append(0)
        s_bina[:2] = [1, 0]
    else:
        s_bina.insert(0, 1)
        s_bina[-2:] = [1, 0]

    q = ''.join(map(str, s_bina))

    res = int(q, 2)
    if res > 51:
        c.append(i)

print(min(c))
"""
# 6
"""
count = 0
def semir(n):
    ns = ''
    while n > 0:
        q = n % 7
        ns = str(q) + ns
        n //= 7
    return ns


for i in range(100, 1000):
    sem = semir(i)
    if sem.count('5') >=2:
        count += 1
print(count)
"""
#8
# pip install xlrd
"""
import pandas as pd

df = pd.read_excel('8.xls')

def check_conditions(row):
    numbers = list(row)

    numbers.sort(reverse=True)

    if numbers[0] <= numbers[1] * numbers[2] * numbers[3] and numbers.count(numbers[0]) == 2 and len(set(numbers)) == 3:
        return True
    else:
        return False

count = df.apply(check_conditions, axis=1).sum()

print(count)
"""
#10
"""
def replace_substring(s, v, w):
    idx = s.find(v)
    if idx != -1:
        return s[:idx] + w + s[idx+len(v):]
    else:
        return s

s = "3" * 8 + "5" * 25

while "35" in s or "355" in s or "3555" in s:

    if "35" in s:
        s = replace_substring(s, "35", "3")

    elif "355" in s:
        s = replace_substring(s, "355", "3")

    else:
        s = replace_substring(s, "3555", "5")

print(s)
"""
# 12
"""
with open('12-1.txt', 'r') as f:
    shusla = [int(num) for num in f.readlines()]
    print(shusla)
N = min(i for i in shusla if i % 11 == 0)

count = 0
mini_sumi = 558587526547

for i in range(len(shusla) - 1):
    if shusla[i] % N == 0 or shusla[i + 1] % N == 0:
        count += 1
        mini_sumi = min(mini_sumi, shusla[i] + shusla[i + 1])

print("Количество пар элементов:", count)
print("Минимальная из сумм элементов таких пар:", mini_sumi)
"""