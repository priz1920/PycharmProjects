
def choice_sort(A):
    N = len(A)
    for i in range(1, N):
        for k in range(i, 0, -1):
            if A[k] < A[k-1]:
                A[k], A[k-1] = A[k-1], A[k]





def test_sort():
    A = [2, 4, 1, 5, 3]
    A_sorted = [1, 2, 3, 4, 5]
    choice_sort(A)
    if A == A_sorted:
        print("OK")
    else:
        print("FAIL")
    print(A)

test_sort()
