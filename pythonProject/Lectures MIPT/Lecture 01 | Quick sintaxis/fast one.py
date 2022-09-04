"""
x = int(input("Введи X:"))
while x > 0:
    y = x
    while y > 0:
        print(y)
        y -= 1
    x -= 1
    print("X теперь=", x)
print("STOP")
"""

"""
for x in 1, 5, 2, 4, 3:
    print(x**2)
    """

"""
flag = False
N = int(input("kolichestvo:"))
for i in range(N):
    x = int(input("chislo:"))
    flag = (x % 10 == 0) or flag
print(flag)

"""

"""
a = "Все числа деляться на 10"
flag = True
N = int(input("kolichestvo:"))

for i in range(N):
    x = int(input("chislo:"))
    flag = flag and (x % 10 == 0)

if not flag:
    a = "Не все числа деляться на 10"

print(a)
"""

"""
x = int(input("INPUT PLEASE:"))
if x % 2 == 0:
    print("DA")
if x % 3 == 0:
    print("da")
if x == 1:
    print("one")
    x += 1
if x == 2:
    print("two")
if x == 1 or x == 2:
    print("dA")
if x % 2 == 0:
    if x % 3 == 0:
        print("Делится на 6")
if x % 2 == 0 and x % 3 == 0:
        print("Делится на 6!!!")
"""

"""
x = int(input("Vvedi chislo:"))
if x < 0:
    print("A")
elif x < 5:
    print("B")
elif x < 10:
    print("C")
else:
    print("D")
"""

"""
x = int(input("Vvedi chislo X:"))
y = int(input("Vvedi chislo Y:"))
if y > 0:
    if x > 0:
        print("I")
    else:
        print("II")
else:
    if x < 0:
        print("III")
    else:
        print("IV")
        
"""


# Перевод в заданную систему счисления введенного числа
"""
while True:
    print("\n")
    x = int(input("vvedi :"))
    base = 2
    digit = 0
    while x > 0:
        digit = x % base
        print(digit, end = "")
        x //= base
"""

"""
def hello (name = "DUDE"):
    print("Hello", name)
x = str(input("what is you name? ___ :"))
hello(x)
"""

"""
def max2(x, y):
    if x > y:
        return x
    return y


def max3(x, y, z):
    return max2(x, max2(y, z))


a = input("pervoe: ")
b = input("vtoroe: ")
c = input("tretie: ")
#max2(b, c)
print(max3(a, b, c))
"""

"""
def hello_separated(name = "World", separator = "-"):
    print("Hello,", name, sep=separator)

hello_separated("John", separator=" {!!!!***} ")

"""

"""
class Goat:
    def __init__(self):
        self.legs = 4
        self.name = name
g = Goat("Nutka")
"""
"""
s = set('solo')
print(s)
"""
"""
text = input()
a = text.split()
print(int(a[0])+int(a[1]))
"""

"""
a = int(input())
x = input()
b = int(input())
if a > b and x == ">":
    print("YES")
elif a < b and x == "<":
    print("YES")
else:
    print("NO")
"""



x = int(input())
y = int(input())
z = int(input())
c = max(x, y, z)
a = b = 0
if c == x:
    a = y
    b = z
elif c == y:
    a = x
    b = z
else:
    a = x
    b = y

if c < a + b:
    if c**2 == a**2 + b**2:
        print("right")
    elif c**2 < a**2 + b**2:
        print("acute")
    elif c**2 > a**2 + b**2:
        print("obtuse")
else:
    print("impossible")
