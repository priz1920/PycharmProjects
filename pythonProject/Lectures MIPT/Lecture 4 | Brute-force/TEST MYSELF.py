a = int(input())


def is_simple_number(x):
    """ Проверяет, является ли
    введенное число простым
    """
    if x <= 0:
        print("Не шути со мной!\nВведите натуральное число!")
    else:
        divisor = 2
        while divisor < x:
            if x % divisor == 0:
                return print(x, "- не является простым")
            divisor += 1
        print(x, "- простое")


#is_simple_number(a)


def factorize_number(x):
    """ Раскладывает заданное число
    на простые делители
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1
    print(x)

factorize_number(a)

