# from turtle import *
# k = 10
# left(90)
# tracer(0)
# screensize(2000,2000)
# for _ in range(2):
#     forward(35*k)
#     right(90)
#     forward(20*k)
#     right(90)
# penup()
# forward(18*k)
# right(270)
# pendown()
#
# for _ in range(2):
#     forward(45*k)
#     right(90)
#     forward(23*k)
#     right(90)
# penup()
# for x in range(-20,20):
#     for y in range(-20,20):
#         goto(x*k,y*k)
#         dot()
# done()
import turtle

# Настройки экрана
screen = turtle.Screen()
screen.setup(width=800, height=800)
t = turtle.Turtle()
t.speed(0)  # Максимальная скорость


# Функция для выполнения команд
def execute_commands():
    # Повтори 2 [Вперёд 35 Направо 90 Вперёд 20 Направо 90]
    for _ in range(2):
        t.forward(35)
        t.right(90)
        t.forward(20)
        t.right(90)

    # Поднять хвост
    t.penup()

    # Вперёд 18 Направо 270
    t.forward(18)
    t.right(270)

    # Опустить хвост
    t.pendown()

    # Повтори 2 [Вперёд 45 Направо 90 Вперёд 23 Направо 90]
    for _ in range(2):
        t.forward(45)
        t.right(90)
        t.forward(23)
        t.right(90)


# Выполняем команды
execute_commands()

# Завершаем выполнение
t.hideturtle()  # Скрыть черепаху после выполнения
turtle.done()  # Закрыть окно по клику
