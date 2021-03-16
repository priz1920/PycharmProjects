""" выводит таблицу степеней для n чисел"""

n = int(input("Введите число:"))

for k in range(2, n+1):
    chislo = [k ** i for i in range(2, n + 1)]
    print(k, chislo)
