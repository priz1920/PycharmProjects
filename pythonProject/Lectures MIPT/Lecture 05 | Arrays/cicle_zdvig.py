def zdvig_left(A:list,N:int):
    tmp=A[0]
    for k in range(N-1):
        A[k] = A[k+1]
    A[N-1] = tmp


def zdvig_right(A:list,N:int):
    tmp=A[N-1]
    for k in range(N-2,-1,-1):
        A[k+1]=A[k]
    A[0]=tmp



def test_zdvig_left():
    A1 = [1, 2, 3, 4, 5]
    print(A1)
    zdvig_left(A1,5)
    print(A1)
    if A1 == [2, 3, 4, 5, 1]:
        print("#test1 - ok")
    else:
        print("test1 - fail")


def test_zdvig_right():
    A2 = [1, 2, 3, 4, 5]
    print(A2)
    zdvig_right(A2,5)
    print(A2)
    if A2 == [5, 1, 2, 3, 4]:
        print("#test2 - ok")
    else:
        print("test2 - fail")


test_zdvig_left()
test_zdvig_right()
