from turtle import *
def rs(a):
    screensize(2000,2000)
    left(90)
    tracer(0)
    k = 50
    penup()
    colo = ['black','red','orange','pink']
    for i in range(len(a)):
        for x,y in a[i]:
            goto(x*k,y*k)
            dot(6,colo[i])
def rs2(a):
    screensize(2000,2000)
    left(90)
    tracer(0)
    k = 50
    penup()
    colo = ['red','orange','pink']
    for i in range(len(a)):
        x,y = a[i][0],a[i][1]
        goto(x * k, y * k)
        dot(6, colo[i])