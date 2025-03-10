f = open('2')
n, k = map(int,f.readline().split())
data = []
for s in f:
    start_zan, konec_zan = map(int, s.split())
    data.append([start_zan,konec_zan])
data.sort()
# print(data)
mesto_gde_har_disk = [0]*k
failov_zaap, idx_pos_disk = 0,0
for start_zan, konec_zan in data:
    for j in range(k):
        if start_zan>mesto_gde_har_disk[j]:
            mesto_gde_har_disk[j] = konec_zan + 1
            failov_zaap += 1
            idx_pos_disk = j + 1
            break
print(mesto_gde_har_disk)
print(failov_zaap, idx_pos_disk)