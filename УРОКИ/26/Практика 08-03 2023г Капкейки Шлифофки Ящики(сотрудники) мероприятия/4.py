f = open('4')
n = int(f.readline())
sh_datails = []
okah_detals = []
for i in range(n):
    sh,ok = map(int,f.readline().split())
    if sh < ok:
        sh_datails.append([sh, i + 1])
    else:
        okah_detals.append([ok,i+1])
print(sh_datails)
print(okah_detals)
print(max(sh_datails), max(okah_detals))
print(len(sh_datails))