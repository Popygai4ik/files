f = open("2")

n = int(f.readline())

day = [0] * 86400

for s in f:
    start, end = map(int, s.split())
    day[start] += 1
    day[end + 1] -= 1
current_process = \
    max_process = max_piks = 0
res = [0] * 86400
for minute in range(len(day)):
    current_process += day[minute]
    res[minute] = current_process
print(max(res[8*60*60:14*60*60 + 1]))
print(res[8*60*60:14*60*60 + 1].count(max(res[8*60*60:14*60*60 + 1])))
n = int(f.readline())

time_start, time_end = 8 * 60 * 60, 14 * 60 * 60

process = [0] * 86401

for i in range(n):

    start, end = map(int, f.readline().split())

    process[start] += 1

    process[end] -= 1



current_process = max_process = max_length = 0

for second in range(len(process)):

    current_process += process[second]



    if time_start <= second <= time_end:

        if current_process > max_process:

            max_process = current_process

            max_length = 1

        elif current_process == max_process:

            max_length += 1



print(max_process, max_length)