# Определить вид треугольника
"""
a = int(input())
b = int(input())
c = int(input())
tr = [a, b, c]
C = max(tr)
tr.remove(C)
A = min(tr)
tr.remove(A)
B = tr[0]
if A + B > C and a > 0 and b > 0 and c > 0:
    if C ** 2 == A ** 2 + B ** 2:
        print("right")
    elif C ** 2 > A ** 2 + B ** 2:
        print("obtuse")
    else:
        print("acute")
else:
    print("impossible")
"""

# Среднее значение последовательности, заканчивающейся нулем
"""
n = int(input())
A = []
while True:
    if n != 0:
        A.append(n)
        n = int(input())
    else:
        break
summa = 0
for i in range(len(A)):
    summa += A[i]
srednee = round(summa/len(A), 2)
print(srednee)
"""

# Поиск максильного четного числа в последовательности
"""
n = int(input())
A = []
while True:
    if n != 0:
        A.append(n)
        n = int(input())
    else:
        break
even_A = []
for i in range(len(A)):
    if A[i] % 2 == 0:
        even_A.append(A[i])
if len(even_A) > 0:
    print(max(even_A))
else:
    print(0)
"""

# Самое частое число
"""
N = int(input())
A = []
for i in range(N):
    n = int(input())
    A.append(n)
count_A = {}
for i in range(len(A)):
    x = A.count(A[i])
    count_A.update({A[i]: x})
maximum = max(count_A.values())
change_count_A = {a: b for b, a in count_A.items()}
result = change_count_A.get(maximum)
print(result)
"""

# Скалярное произведение
"""
def dot_product(N, vector1, vector2):
    product_count = []
    for i in range(N):
        product = vector1[i] * vector2[i]
        product_count.append(product)
    return sum(product_count)
"""

# Максимум неполного массива
"""
n = int(input())
A = [n]
maximum = n
while True:
    n = int(input())
    if n != 0:
        A.append(n)
        if maximum < A[0]:
            maximum = A[0]
        if len(A) > 5:
            A.pop(0)
    else:
        break
print(maximum)
"""

# Грузовик
"""
weight_truck = int(input())
height_truck = int(input())
weight_piano = int(input())
height_piano = int(input())
weight_fridge = int(input())
height_fridge = int(input())
max_weight_bridge = int(input())
max_height_tunnel = int(input())
total_weight = weight_truck + weight_fridge + weight_piano
total_height = height_truck + max(height_fridge, height_piano)
flag_tunnel = False
flag_bridge = False

for i in range(2):
    if max_height_tunnel >= total_height and not flag_tunnel:
        flag_tunnel = True
        total_weight = total_weight - weight_fridge
    elif not flag_tunnel:
        flag_tunnel = False
    if max_weight_bridge >= total_weight and not flag_bridge:
        flag_bridge = True
        total_height = height_truck + height_fridge
    elif not flag_bridge:
        flag_bridge = False

if flag_tunnel and flag_bridge:
    print("YES")
else:
    print("NO")
"""

# Первое число трибоначчи, превосходящее заданное
"""
N = int(input())
tribonachi = [0, 0, 1]
i = 3
while tribonachi[i-1] <= N:
    tribonachi_new = tribonachi[i-3] + tribonachi[i-2] + tribonachi[i-1]
    tribonachi.append(tribonachi_new)
    i += 1
if N < 0:
    print(0)
else:
    print(i-1)

"""

# Раскраска прямой
"""
N = int(input())  # 0 <= N <= 100 - количество дней
fence = []
day = [0, 0, 0]
for k in range(N):
    for i in range(3):
        day[i] = int(input())
    if day[0] > day[1]:     # #   ЕСЛИ КРАСЯТ ЗАБОР В ОБЕ СТОРОНЫ!!!!
        day[0], day[1] = day[1], day[0]
    # print("день", k, day)
    # if day[0] > day[1]:   #   ЕСЛИ КРАСЯТ ЗАБОР ТОЛЬКО СЛЕВА НАПРАВО!!!!
    #     continue

    if len(fence) == 0:  # Если рассматриваем первый день
        fence.append(day)  # Вставить в забор

    elif day[0] <= fence[0][0]:  # Иначе если (день не первый) и левая доска дня меньше левой доски первого дня
        fence.insert(0, day)  # Вставить день в начало
        # print("левая доска в день ВСТАВКА В НАЧАЛО", k, day[0])

        while True and len(fence) > 1:
            if day[1] < fence[1][0]:
                break
            elif fence[1][0] <= day[1] < fence[1][1]:  # Если граница правого дня находится в диапазоне следующего
                fence[1][0] = day[1] + 1  # Изменить диапазон следующего
                break
            elif day[1] >= fence[1][1]:  # Иначе если граница правого дня превышает диапазон следующего
                fence.pop(1)  # Удалить следующий диапазон
        # print("забор в день", k, fence)
    else:
        # print("левая доска в день", k, day[0])
        flag = 0
        for t in range(len(fence)):
            # print("в цикле", flag)
            if fence[t-1][1] < day[0] <= fence[t][0] and t != 0 and flag == 0:
                fence.insert(t, day)
                flag = 1
                while True and t + 2 <= len(fence):  # t и так не привысит длину забора
                    if day[1] < fence[t + 1][0]:
                        break
                    elif fence[t + 1][0] <= day[1] < fence[t + 1][1]:  # Если граница правого дня находится в диапазоне следующего
                        fence[t + 1][0] = day[1] + 1  # Изменить диапазон следующего
                        break
                    elif day[1] >= fence[t+1][1]:  # Иначе если граница правого дня превышает диапазон следующего
                        fence.pop(t + 1)  # Удалить следующий диапазон
                break
            elif fence[t][0] < day[0] <= fence[t][1] and flag == 0:  # Если левая доска меньше правой предыдущей
                fence.insert(t + 1, day)  # Вставить день следующим
                right_plank = fence[t][1]  # Запомнить правую доску предыдущего дня
                fence[t][1] = day[0] - 1  # Уменьшить диапозон предыдущего дня
                flag = 1
                # print("флаг внутри успешного цикла", flag)
                # print("Suссess", fence[t][1])
                # Если дневные доски перекрашивают предыдущий день

                if day[1] < right_plank:  # Если правая доска меньше правой доски предыдущего дня
                    new_range = [day[1] + 1, right_plank, fence[t][2]]  # Новый диапазон
                    fence.insert(t + 2, new_range)  # Вставить на следующее место
                    break
                else:
                    flag1 = 0
                    while flag1 == 0 and t + 3 <= len(fence):
                        if day[1] < fence[t + 2][0]:  # Если правая доска меньшн левой доски следующей, ничего не делаем
                            flag1 = 1
                        elif fence[t + 2][0] <= day[1] < fence[t + 2][1]:  # Если правая доска в диапозоне следующего дня
                            fence[t + 2][0] = day[1] + 1  # Меняем диапозон следующего дня
                            flag1 = 1
                        elif day[1] >= fence[t + 2][1]:  # Иначе если праввая доска больше либо равна правой доски следующего дня

                            fence.pop(t + 2)  # Удаляем следующий день
                            print("Flag 0")
                break
        if flag == 0:
            # print("если цикл не удался", flag)
            fence.append(day)
    day = [0, 0, 0]
    # print("забор в день", k, fence)
    # print("номер правой доски в день", k, fence[k][1])

M = int(input())  # 0 < M <= 100 - число интересующих Васю дощечек
search = []
for j in range(M):
    plank = int(input())  # Номера интересующих дощечек
    search.append(plank)
result = []

#print("fence", fence)
#print("search", search)

for j in range(M):
    flag2 = 0
    for k in range(len(fence)):
        if fence[k][0] <= search[j] <= fence[k][1] and flag2 == 0:
            res = fence[k][2]
            result.append(res)
            flag2 = 1
    if flag2 == 0:
        result.append(0)
print(*result)
"""

# Наибольший общий делитель алгоритм Евклида
"""
x = int(input())
y = int(input())


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


print(gcd(x, y))
"""