def generate_numbers(N:int, M:int, prefix=None):
    """Генерирует все числа (с лидирующими незначащими нулями)
    в N-ричной системе счисления (N <= 10)
    Длины M."""
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

def gen_bin(M, prefix=""):
    """Тоже самое, проще для понимания, только для двоичной системы"""
    if M == 0:
        print(prefix)
        return
    """else:
        gen_bin(M - 1, prefix + "0")
        gen_bin(M - 1, prefix + "1")"""
    for digit in "0", "1":
        gen_bin(M - 1, prefix + digit)

#generate_numbers(3, 3)
#gen_bin(3)



