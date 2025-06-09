from turtle import *

def ris(a):
    left(90)
    tracer(0)
    k = 20
    penup()
    colo = ['red','black','blue']
    screensize(2000,2000)
    for i in range(len(a)):
        for x,y in a[i]:
            setpos(x*k,y*k)
            dot(5, colo[i])

def ris2(a):
    left(90)
    tracer(0)
    k = 20
    penup()
    colo = ['pink','green','gray']
    screensize(2000,2000)
    for i in range(len(a)):
        x,y = a[i]
        setpos(x*k,y*k)
        dot(10, colo[i])