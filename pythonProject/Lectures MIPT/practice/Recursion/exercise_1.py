# Упражнение №1: длина рекурсии
import sys
z = 0


def fac(n):
    global z  # Обращаемся к переменной определенной вне функции
    z += 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)


print(fac(5))
print("Количество вызовов рекурсии:", z)

# Стек вызовов рекурсии
print("Максимальная глубина стека вызовов рекурсии:", sys.getrecursionlimit())
