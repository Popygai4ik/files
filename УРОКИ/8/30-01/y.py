import itertools
# с = 0
# for s in itertools.permutations('ПОЕШЬ', r=5):
#     w = ''.join(s)
#     if s.count('Ь') == 1 and  w[-1] != 'Ь' and w[0] != 'Ь' and 'ЬЕ' not in w and 'ЕЬ' not in w:
#         с +=1
# print(с)
# с = 0
# for s in itertools.permutations('МЕДИА', r=5):
#     w = ''.join(s)
#     if w.count('ЕДА') == 0 and   w[0] != 'А':
#         с +=1
# print(с)


N = int(input())

matritsa = [[0] * N for _ in range(N)]
cur_shislo = 1

for i in range(N):
    if i % 2 == 0:
        for j in range(N):
            matritsa[i][j] = cur_shislo
            cur_shislo += 1
    else:
        for j in range(N - 1, -1, -1):
            matritsa[i][j] = cur_shislo
            cur_shislo += 1
for s in matritsa:
    print(" ".join(map(str, s)))
# R, D, M = map(int, input().split())
# print(R * D * M)