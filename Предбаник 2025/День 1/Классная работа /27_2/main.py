from turtle import *

def ris(a):
    k = 20
    tracer(0)
    left(90)
    penup()
    colors = ['red','blue','black']
    for i in range(len(a)):
        for t1 in a[i]:
            x,y = t1
            goto(x*k, y*k)
            dot(5,colors[i])
def ris2(a):
    k = 20
    tracer(0)
    left(90)
    penup()
    i = 0
    colors = ['black','red','blue']
    for t1 in a:
        print(t1)
        x,y = t1
        goto(x*k, y*k)
        dot(5,colors[i])
        i += 1