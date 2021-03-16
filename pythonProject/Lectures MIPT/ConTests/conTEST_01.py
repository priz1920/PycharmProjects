"""
# Ход Ферзя
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x2 == x1 or y2 == y1 or abs(x2 - x1) == abs(y2 - y1):
    print("YES")
else:
    print("NO")
"""

"""
#Високосный год

n = int(input())
if n % 400 == 0:
    print("YES")
elif n % 4 == 0 and n % 100 != 0:
    print("YES")
else:
    print("NO")
"""

"""
# Квадраты чисел
n = int(input())
z = int(n**0.5)
A = []
for i in range(1, z+1):
    A.append(i**2)
print(*A)
"""

"""
#Двоичный логарифм
n = int(input())
k = 1
i = 0
while k < n:
    k = k * 2
    i += 1
print(i)
"""


"""
#Длина последовательности
n = int(input())
i = 0
if n == 0:
    print(0)
else:
    while n > 0:
        n = int(input())
        i += 1
        if n == 0:
            print(i)
"""

"""
#Сумма введенной последовательности

n = int(input())
i = n
if n == 0:
    print(0)
else:
    while n != 0:
        n = int(input())
        i += n
        if n == 0:
            print(i)
"""

"""
#Количество четных элементов в массиве
n = int(input())
N = [n]
k = 0
while n != 0:
    n = int(input())
    N.append(n)
    if n == 0:
        break
for i in range(len(N)):
    if N[i] % 2 == 0 and N[i] != 0:
        k += 1
print(k)
"""

"""
#Максимум последовательности

n = int(input())
N = [n]
k = 0
while n != 0:
    n = int(input())
    N.append(n)
    if n == 0:
        break
k = max(N)
print(k)
"""
"""
#Количество элементов, равных максимуму

n = int(input())
N = [n]
m = 0
while n != 0:
    n = int(input())
    N.append(n)
    if n == 0:
        break
k = max(N)
for i in range(len(N)):
    if N[i] == k:
        m += 1
print(m)
"""
