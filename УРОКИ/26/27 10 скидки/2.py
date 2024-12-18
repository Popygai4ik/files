f = open('2.txt')
n= int(f.readline())
a = [int(s) for s in f]
a.sort(reverse=True)
s1 = sum(a[:(n//3)])*0.5
a.sort()
s2 = sum(a[:(n//3)])*0.5
print(sum(a) - s1, sum(a) - s2)