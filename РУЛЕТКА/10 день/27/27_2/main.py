from  turtle import *
def ris(a):
    left(90)
    penup()
    tracer(0)
    screensize(2000,2000)
    k = 25
    colo = ['red','blue','pink','black','orange']
    for i in range(len(a)):
        for x, y in a[i]:
            goto(x*k,y*k)
            dot(5,colo[i])
def ris2(a):
    left(90)
    tracer(0)
    screensize(2000,2000)
    k = 25
    colo = ['orange','black','gray','purple','pink']
    for i in range(len(a)):
        x, y  = a[i]
        goto(x*k,y*k)
        dot(10,colo[i])