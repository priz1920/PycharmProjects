

"""
def frequency_sort(A):
    N = len(A)
    F = [0] * 6
    for i in range(N):
        F[A[i]] += 1
    #A = []
    del A[:]
    for k in range(len(F)):
        A.extend(F[k] * [k])
"""

def frequency_sort(A):
    #A = []
    del A[:]





def test_sort():
    A = [2, 4, 1, 5, 3, 2, 4, 1, 5, 3, 2, 4, 1, 5, 3]
    A_sorted = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    frequency_sort(A)
    print(A)
    if A == A_sorted:
        print("OK")
    else:
        print("FAIL")


test_sort()
