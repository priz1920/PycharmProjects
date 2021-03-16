
N = int(input())  # 0 <= N <= 100 - количество дней
fence = []
day = [0, 0, 0]
#добавляю комит
for k in range(N):
    for i in range(3):
        day[i] = int(input())
    if day[0] > day[1]:
        day[0], day[1] = day[1], day[0]
    print("день", k, day)

    if k == 0:  # Если рассматриваем первый день
        fence.append(day)  # Вставить в забор

    elif day[0] <= fence[0][0]:  # Иначе если (день не первый) и левая доска дня меньше левой доски первого дня
        fence.insert(0, day)  # Вставить день в начало
        print("левая доска в день ВСТАВКА В НАЧАЛО", k, day[0])

        while True and len(fence) > 1:
            if day[1] < fence[1][0]:
                break
            elif fence[1][0] <= day[1] < fence[1][1]:  # Если граница правого дня находится в диапазоне следующего
                fence[1][0] = day[1] + 1  # Изменить диапазон следующего
                break
            elif day[1] >= fence[1][1]:  # Иначе если граница правого дня превышает диапазон следующего
                fence.pop(1)  # Удалить следующий диапазон
        print("забор в день", k, fence)
    else:
        print("левая доска в день", k, day[0])
        flag = 0
        for t in range(len(fence)):
            print("в цикле", flag)
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
                print("флаг внутри успешного цикла", flag)
                print("Suссess", fence[t][1])
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
            print("если цикл не удался", flag)
            fence.append(day)
    day = [0, 0, 0]
    print("забор в день", k, fence)
    # print("номер правой доски в день", k, fence[k][1])

M = int(input())  # 0 < M <= 100 - число интересующих Васю дощечек
search = []
for j in range(M):
    plank = int(input())  # Номера интересующих дощечек
    search.append(plank)
result = []

print("fence", fence)
print("search", search)

for j in range(M):
    flag2 = 0
    for k in range(len(fence)):
        if fence[k][0] <= search[j] <= fence[k][1] and flag2 == 0:
            res = fence[k][2]
            result.append(res)
            flag2 = 1
    if flag2 == 0:
        result.append(0)
print("result", *result)
