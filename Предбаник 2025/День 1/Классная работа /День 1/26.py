f = open('26.2_5xUhRUh.txt')
# f = open('t')
n = f.readline()
a = [int(s) for s in f]
a.sort(reverse=True)
# print(len(a[:3333]))
print(sum(a)- sum(a[:len(a)//3]))
s = 0
for i in range(len(a)):
    if (i + 1) % 3 == 0:
        s+= a[i]
print(sum(a)- s)