
n = int(input("Введите количество строк треугольника Паскаля:"))

def pascal_triangle(n):
    """ Выводит первые n строк треугольника Паскаля.
        Использует временные массивы
        """
    row = [1]
    y = [0]
    for x in range(n):
        print(row)
        tmp1 = row + y
        tmp2 = y + row
        tmp3 = [0] * len(tmp1)
        for t in range(len(tmp1)):
            tmp3[t] = tmp1[t]+tmp2[t]
        row = tmp3

pascal_triangle(n)