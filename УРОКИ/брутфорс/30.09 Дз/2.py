from itertools import *
f = open('2.txt')
def per(n):
    return n +1
def vto(n):
    return n *2
def tr(n):
    return n *3

n = int(f.readline())
spisok =[]
for s in f:
    for cnt in range(1, int(s)+1):
        for comd in product('123', repeat=cnt):
            shisl = n
            for k in comd:
                if k == '1':
                    shisl += per(shisl)
                elif k == '2':
                    shisl += vto(shisl)
                elif k == '3':
                    shisl += tr(shisl)
            if shisl == int(s):
                spisok.append(shisl)
                print(shisl)
                break
print(sum(spisok))

