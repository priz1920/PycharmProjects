
N = int(input())  # 0 <= N <= 100 - количество дней
fence = []
day = [0, 0, 0]
for k in range(N):
    for i in range(3):
        day[i] = int(input())
    if day[0] > day[1]:
        day[0], day[1] = day[1], day[0]
    if k == 0:  # Если рассматриваем первый день
        fence.append(day)  # Вставить в забор
    elif day[0] < fence[0][0]:  # Иначе если (день не первый) и левая доска дня меньше левой доски первого дня
        fence.insert(0, day)  # Вставить день в начало
        flag0 = 0
        while flag0 == 0 and len(fence) > 1:
            if day[1] < fence[1][0]:
                flag0 = 1
            elif fence[1][0] < day[1] < fence[1][1]:  # Если граница правого дня находится в диапазоне следующего
                fence[1][0] = day[1] + 1  # Изменить диапазон следующего
                flag0 = 1
            elif day[1] > fence[1][1]:  # Иначе если граница правого дня превышает диапазон следующего
                fence.pop(1)  # Удалить следующий диапазон
    else:
        flag = 0
        for t in range(k):
            if day[0] < fence[t][1] and flag == 0:  # Если левая доска меньше правой предыдущей
                fence.insert(t + 1, day)  # Вставить день следующим
                right_plank = fence[t][1]  # Запомнить правую доску предыдущего дня
                fence[t][1] = day[0] - 1  # Уменьшить диапозон предыдущего дня
                flag = 1
                # Если дневные доски перекрашивают предыдущий день
                if day[1] < right_plank:  # Если правая доска меньше правой доски предыдущего дня
                    new_range = [day[1] + 1, right_plank, fence[t][2]]  # Новый диапазон
                    fence.insert(t + 2, new_range)  # Вставить на следующее место
        if flag == 0:
            fence.append(day)
    day = [0, 0, 0]

M = int(input())  # 0 < M <= 100 - число интересующих Васю дощечек
search = []
for j in range(M):
    plank = int(input())  # Номера интересующих дощечек
    search.append(plank)
result = []


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

