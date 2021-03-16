n = int(input("Введите количество строк треугольника Паскаля:"))

def pascal_triangle(n):
    """ Выводит первые n строк треугольника Паскаля.
        Использует функцию zip"""
    row = [1]
    y = [0]
    for x in range(n):
        print(row)
        row = [left + right for left, right in zip(row + y, y + row)]

pascal_triangle(n)
