import random

def hoar_sort(A):
    if len(A) <= 1:
        return
    barriaer = A[0]
    L = []
    M = []
    R = []
    for x in A:
        if x < barriaer:
            L.append(x)
        elif x == barriaer:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1

sort = [random.randint(1, 20) for i in range(2, 12)]
print(sort)
hoar_sort(sort)
print(sort)