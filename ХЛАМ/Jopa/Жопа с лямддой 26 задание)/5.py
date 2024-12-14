f = open("5.txt")

n, m, k = map(int, f.readline().split())

data = [list(map(int, f.readline().split())) for i in range (n)]

data.sort(key = lambda x : (x[0], -x[1]))

status = [[0 for j in range (m + 1)] for i in range (k + 1)]

succes_fans = 0

for start, stop in data:

    for i in range (1, k + 1):

        if status[i][start] == 0:

            for j in range (start, stop):

                status[i][j] = 1

            succes_fans += 1

            break

cnt_soldout = 0

for i in range (1, m + 1):

    cnt_occupied = 0

    for j in range (1, k + 1):

        cnt_occupied += status[j][i]

    if cnt_occupied == k:

        cnt_soldout += 1

print(succes_fans, cnt_soldout)