f = open('1')
n = int(f.readline())
koriki = []
for korz in f:
    razmer = int(korz)
    koriki.append(razmer)

koriki.sort(reverse=True)
cake = []
cake.append(koriki[0])
# print(koriki)
for kor in koriki:
    if (cake[-1] - kor) >= 7:
        cake.append(kor)

print(len(cake), cake[-1])