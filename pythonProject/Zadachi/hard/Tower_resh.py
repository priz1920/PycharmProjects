import math
import decimal
from decimal import *



"""
A1 = [3,99,3,3]
A2 = [3,3,3,4]
A3 = [3,3,3,5]
A4 = [3,3,3,6]
A5 = [3,3,3,7]
A6 = [3,3,3,8]
A7 = [3,3,3,9]
A8 = [3,3,3,10]
A9 = [3,3,3,11]
A10 = [3,10,3,12]
"""
file = open("input", "r")
#count = file.readlines()
#print(count)

"""i = 0
for line in file:
    FFF = list(line)
    i += 1

FFF.remove("\n")
    
for i in range(len(FFF)):
    if FFF[i] == None:
        FFF.pop(i)    
    print(i, FFF)
    i += 1"""

A1 = [2,30,2]
A2 = [2,2,30]
A3 = [2,3,5]
A4 = [2,3,6]
A5 = [2,3,7]
A6 = [2,3,8]
A7 = [2,3,9]
A8 = [2,3,10]
A9 = [2,3,11]
A10 = [2,3,12]
A = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10]

N = []

def logarifm(m, A):
    for i in range(m-1, -1, -1):
        if i == 0:
            return math.log1p(A[i])
        result = math.log1p(A[i] * logarifm(m-1, A))
        if result not in N:
            N.append(result)
        return math.log1p(A[i] * logarifm(m-1, A))


"""
def logarifm(m, A):
    for i in range(m-1, -1, -1):
        if i == 0:
            return Decimal(math.log((A[i]), 2))
        result = Decimal(math.log((A[i] * logarifm(m-1, A)), 2))
        if result not in N:
            N.append(result)
        return Decimal(math.log((A[i] * logarifm(m-1, A)), 2))
"""


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


res1 = logarifm(len(A1), A1)
res2 = logarifm(len(A2), A2)
res3 = logarifm(len(A3), A3)
res4 = logarifm(len(A4), A4)
res5 = logarifm(len(A5), A5)
res6 = logarifm(len(A6), A6)
res7 = logarifm(len(A7), A7)
res8 = logarifm(len(A8), A8)
res9 = logarifm(len(A9), A9)
res10 = logarifm(len(A10), A10)

res = [res1, res2, res3, res4, res5, res6, res7, res8, res9, res10]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ob = dict(zip(res, num))

#print(ob)
print(list(ob[res[i]] for i in range(len(res))))
"""try:
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    print(res5)
    print(res6)
    print(res7)
    print(res8)
    print(res9)
    print(res10)

except:
    print("не могу посчитать")
"""
print(res)

hoar_sort(res)

print(res)
print(list(ob[res[i]] for i in range(len(res))))

file.close()

print()