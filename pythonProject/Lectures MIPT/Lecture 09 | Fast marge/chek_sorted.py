import random

def check_sorted(A, ascending = True):
    """Проверка отсортированности за O(len(A))"""
    flag = True
    s = 2 * int(ascending) - 1
    for i in range(0, len(A)-1):
        if s * A[i] > s * A[i+1]:
            flag = False
            break
    return flag


sort = [random.randint(1, 20) for i in range(2, 12)]
sort = [1,2,3,4,5,6,7,8]
print(sort)

print(check_sorted(sort))