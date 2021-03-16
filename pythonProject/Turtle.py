import turtle
import math

#Окружность
"""

turtle.shape('turtle')
turtle.penup()
#turtle.stamp()
turtle.forward(100)
turtle.left(90)
turtle.width(3)
turtle.pendown()
turtle.color("blue", "green")
turtle.begin_fill()
for i in range(72):
    turtle.forward(10)
    turtle.left(5)
turtle.end_fill()
turtle.penup()
turtle.goto(-10, 0)
turtle.mainloop()
"""

#Вложенные квадраты
"""
turtle.shape('turtle')
x = 0
y = 0
l = 0
for i in range(100):
    x -= 10
    y -= 10
    l += 20
    turtle.penup()
    turtle.goto(x-10, y-10)
    turtle.pendown()
    turtle.forward(l+20)
    turtle.left(90)
    turtle.forward(l+20)
    turtle.left(90)
    turtle.forward(l+20)
    turtle.left(90)
    turtle.forward(l+20)
    turtle.left(90)
turtle.mainloop()
"""

#Паук
"""
turtle.shape('turtle')
u = 0
n = 12
for i in range(n):
    u = 360/n
    turtle.goto(0, 0)
    turtle.left(u)
    turtle.pendown()
    turtle.forward(100)
    turtle.stamp()
    turtle.penup()
turtle.mainloop()
"""

#спираль
"""
import math
turtle.shape('turtle')
x = 0
for i in range(300):
    u = 15
    turtle.forward(x)
    turtle.left(u)
    x += u/(20*2*math.pi)
turtle.mainloop()
"""

#Квадратная спираль
"""
turtle.shape('turtle')
x = 0
for i in range(300):
    u = 90
    turtle.forward(x)
    turtle.left(u)
    x += 10
turtle.mainloop()
"""

# Правильные многоугольники
"""
turtle.shape('turtle')
L = 10
m = 17


def pravilniy(n, a):
    u = (n-2)*180/n
    u1 = 360/n
    r = a/(2*math.sin((2*math.pi)/(2*n)))
    turtle.penup()
    turtle.forward(r-((a-7)/(2*math.sin((2*math.pi)/(2*(n-1))))))
    turtle.left(u/2)
    turtle.pendown()
    for i in range(n):
        turtle.left(u1)
        turtle.forward(a)
    turtle.right(u/2)

for i in range(3, m):
    pravilniy(i, L)
    L += 7


turtle.mainloop()

"""

# Цветок
"""
turtle.shape('turtle')
n = 10
turtle.width(3)


def circle():
    for i in range(72):
        turtle.forward(10)
        turtle.left(5)
    for i in range(72):
        turtle.forward(10)
        turtle.right(5)


for k in range(n):
    turtle.left(45)
    circle()
turtle.mainloop()
"""

# Бабочка
"""
turtle.shape('turtle')
g = 5
n = 17
turtle.width(3)
turtle.left(90)


def circle(f):
    for i in range(72):
        turtle.forward(f)
        turtle.left(5)
    for i in range(72):
        turtle.forward(f)
        turtle.right(5)


for k in range(n):
    circle(g)
    g += 1
turtle.mainloop()
"""

# Пружина
"""
turtle.shape('turtle')

n = 17
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.width(3)
turtle.left(90)

def circle():
    for i in range(37):
        turtle.forward(5)
        turtle.right(5)
    for i in range(35):
        turtle.forward(1)
        turtle.right(5)

for k in range(n):
    circle()
turtle.mainloop()
"""

# Смайлик
"""
turtle.shape('turtle')
g = 5
n = 17
turtle.width(3)
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()

turtle.left(90)


def circle():
    for i in range(72):
        turtle.forward(10)
        turtle.left(5)
turtle.begin_fill()
turtle.color("black", "yellow")
circle()
turtle.end_fill()

turtle.penup()
turtle.goto(-40, 50)
turtle.pendown()
def eye():
    for i in range(72):
        turtle.forward(2)
        turtle.left(5)
turtle.begin_fill()
turtle.color("black", "blue")
eye()
turtle.end_fill()

def eye2():
    for i in range(72):
        turtle.forward(1)
        turtle.left(5)
turtle.begin_fill()
turtle.color("black", "white")
eye2()
turtle.end_fill()

turtle.penup()
turtle.goto(60, 50)
turtle.pendown()

turtle.begin_fill()
turtle.color("black", "blue")
eye()
turtle.end_fill()
turtle.begin_fill()
turtle.color("black", "white")
eye2()
turtle.end_fill()

turtle.penup()
turtle.goto(-10, 25)
turtle.pendown()
turtle.left(180)
turtle.width(15)
turtle.color("green", "black")
turtle.forward(30)

turtle.penup()
turtle.goto(-85, -20)
turtle.pendown()
turtle.width(10)
def lips():
    for i in range(37):
        turtle.forward(6)
        turtle.left(5)
turtle.color("red" ,"black")
lips()

turtle.mainloop()
"""

# Звездочка
"""
turtle.shape("turtle")
n = 5
a = 250
turtle.penup()
turtle.goto(100, 0)
turtle.pendown()
turtle.left(180)
for i in range(n):
    turtle.forward(a)
    turtle.left((180-180/n))

turtle.mainloop()
"""