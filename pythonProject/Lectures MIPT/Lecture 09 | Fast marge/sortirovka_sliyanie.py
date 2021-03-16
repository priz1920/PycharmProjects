import random
n = int(input("Введите число:"))
sortir = [random.randint(1, 1000) for i in range(2, n + 1)]
print(sortir)

def merge(A: list, B: list):
    """Сливает 2 массива в один, сортируя его по возрастанию"""
    C = [0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


def merge_sort(A:list):
    """ Разбивает массив А части, и каждую
        из получившихся частей сортирует и
        сливает с помощью предыдущей функции
        marge"""
    if len(A) <= 1:
        return
    middle = len(A)//2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(middle, len(A))]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]


merge_sort(sortir)
print(sortir)