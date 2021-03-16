import random
x = int(input("Введи количество клеток:"))
cena = [float("-inf"), 0]+[random.randint(1, 20) for i in range(x-2)]


def count_min_cost(n, price: list):
    C = [float("-inf"), price[1], price[1] + price[2]] + [0] * (n-3) #Массив минимально возможных стоимостей достижения клетки
    for i in range(3, n):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C


print("Цена на пункте сбора оплаты", cena)
print("Минимальная стоимость движа", count_min_cost(x, cena))
