
def search_sort(A):
    N = len(A)
    for i in range(N-1):
        for k in range(i+1, N):
            if A[i] > A[k]:
                A[i], A[k] = A[k], A[i]






def test_sort():
    A = [2, 4, 1, 5, 3]
    A_sorted = [1, 2, 3, 4, 5]
    search_sort(A)
    if A == A_sorted:
        print("OK")
    else:
        print("FAIL")


test_sort()
