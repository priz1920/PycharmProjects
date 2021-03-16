"""
vhod = input()
k = vhod.split()
x = int(k[0])
y = int(k[1])
r = int(k[2])
res = (x ** 2 + y ** 2) ** 0.5
if res <= r:
    print("YES")
else:
    print("NO")

    """

# Банковский вклад
"""
vhod = input()
k = vhod.split()
if len(k) != 3:
    print(0)
else:
    x = int(k[0])
    p = int(k[1])
    y = int(k[2])
    i = 0
    p = p / 100
    if x == 0:
        print("Вы должны сделать вклад")
    elif x == 1:
        while x < y:
            x = x + p
            x = round(x, 2)
            i += 1
    else:
        while x < y:
            x = x + p * x
            x = round(x, 2)
            i += 1
    print(i)
"""

# Максимальное число подряд идущих 1
"""
N = int(input())
num = []
dl = []
for i in range(N):
    n = int(input())
    num.append(n)
k = 0
for i in num:
    if i == 1:
        k += 1
    elif i == 0:
        dl.append(k)
        k = 0
dl.append(k)
print(max(dl))
"""

# Обработка массива чисел
"""
num = []
while True:
    n = input()
    if n == "#":
        break
    elif n.find(" ") != -1:
        num111 = list(map(int, n.split()))
        tmp = num111[0]
        for i in range(len(num111)-1):
            num111[i] = num111[i+1]
        num111[len(num111)-1] = tmp
        print(*num111)
        break
    else:
        num.append(int(n))

if len(num) > 1:
    # Среднее последовательности
    sum = 0
    for i in range(len(num)):
        sum += num[i]
    sred = round(sum / len(num), 3)


    # Сумма остатков от деления суммы троек на последнее число тройки:
    sum3list = []
    t = 0
    while t <= (len(num)-3):
        sum3 = num[t]+num[t+1]+num[t+2]
        sum3 = sum3 % num[t+2]
        sum3list.append(sum3)
        t += 3
        sum3 = 0
    sumost = 0
    for i in range(len(sum3list)):
        sumost += sum3list[i]

    print(sred, max(num), min(num), sumost)

"""

# Результаты работы студентов в семестре
"""
num = []
# Количество учеников
k = int(input())
# Простые числа
if k > 100:
    N = k
    A = [True]+[True] * N
    A[0] = A[1] = False
    for k in range(2, N+1):
        if A[k]:
            for m in range(2 * k, N+1, k):
                A[m] = False
    g = []
    for k in range(len(A)):
        if A[k]:
            g.append(k)
    print(*g)
else:
    # Ученик и его оценка
    while True:
        n = input()
        if n == "#":
            break
        else:
            n = n.split()
            n = list(map(int, n))
            num.append(n)

    # Вместе с суммой баллов
    #sumlist = []
    sum1 = 0
    for t in range(k):
        for i in range(len(num)):
            if num[i][0] == t:
                sum1 += num[i][1]
        for i in range(len(num)):
            if num[i][0] == t:
                num[i].append(sum1)
        sum1 = 0

    # Сортируем
    num = sorted(num, key=lambda x: (x[2], -x[0], x[1]), reverse=True)

    # Результат
    res = []
    for i in range(len(num)):
        res.append(num[i][1])

    # Баллы по убыванию
    print(*res)
"""

# Решето Эратосфена
"""
N = int(input())
A = [True] + [True] * N
A[0] = A[1] = False
for i in range(3, N+1):
    for k in range(i*2, N+1, i):
        A[k] = False
res = []
z = 0
for i in range(N+1):
    if A[i]:
        res.append(i)
        z += 1
#print(*res)
print(z)
"""

# Шоколадка
"""
N = int(input())
if N % 2 != 0:
    print(0)
else:
    c = [0] * (N+1)   
    c[0] = 1
    for i in range(2, N+1, 2):
        c[i] = c[i-2] * 3
        for j in range(i - 4, -1, -2):
            c[i] += c[j]*2
    print(c[N])
"""

# Шоколадка быстрый способ
"""
N = int(input())
if N % 2 != 0:
    print(0)
else:
    c = [0] * (N+1)
    cPlus = [0] * (N+1)
    c[0] = 1
    cPlus[0] = 1
    for i in range(2, N+1, 2):
        c[i] = c[i-2] + 2 * cPlus[i-2]
        cPlus[i] = c[i] + cPlus[i-2]
    print(c[N])
"""

# Шоколадка простой способ
"""
N = int(input())
if N % 2 != 0:
    print(0)
else:
    a0 = 1
    a1 = 3
    olda1 = 0
    for i in range(2, N, 2):
        olda1 = a1
        a1 = 4 * a1 - a0
        a0 = olda1
    print(a1)
   
"""

# Степень строки
"""
string = str(input())
k = int(input())
if k == 0:
    print("NO SOLUTION")
elif k > 0:
    string = string * k
    print(string)
else:
    if len(string) % k != 0:
        print("NO SOLUTION")
    else:
        k = -k
        z = 1
        template = string[:int(len(string)/k)]
        for i in range(len(template), len(string), len(template)):
            if string[i:len(template) + i] != template:
                print("NO SOLUTION")
                break
            else:
                z += 1
        if z == len(string)/len(template):
            print(template)
"""


