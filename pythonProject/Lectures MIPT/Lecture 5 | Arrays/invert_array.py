def inver_array(A:list,N:int):
    """Обращение массива (поворот задом-наперед)
    в рамках индексов от 0 до N-1
    """
    for k in range(N//2):
        A[k], A[N-1-k] = A[N-1-k], A[k]
    #pass

def test_invert_array():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    inver_array(A1,5)
    print(A1)
    if A1 == [5, 4, 3, 2, 1]:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [0, 0, 0, 0, 0, 0, 0, 10]
    print(A2)
    inver_array(A2, 8)
    print(A2)
    if A2 == [10, 0, 0, 0, 0, 0, 0, 0]:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

test_invert_array()