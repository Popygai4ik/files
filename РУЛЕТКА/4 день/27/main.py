from turtle import *
def ris(a):
    left(90)
    screensize(4000,4000)
    tracer(0)
    dot()
    k = 10
    penup()
    clor = ['pink','black','orange']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(5,clor[i])
def ris2(a):
    screensize(4000,4000)
    tracer(0)
    dot()
    k = 10
    penup()
    clor = ['black','orange','pink']
    for x,y in a:
        goto(x*k,y*k)
        dot(10,clor[a.index([x,y])])