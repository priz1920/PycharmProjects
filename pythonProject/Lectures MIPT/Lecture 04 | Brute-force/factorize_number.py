

a = int(input("Введите число:"))


def factorize_number(x):
    """Раскладывает число на множители.
    Печатает их на экран.
    х - целое положительное число."""
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1


factorize_number(a)