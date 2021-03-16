"""Фибоначи рекурсия / динамика / в лоб"""

chislo = int(input())
N = [1, 1]


def fib(n):
    if n <= 1:
        return 1
    result = fib(n-1) + fib(n-2)
    if result not in N:
        N.append(result)
    return result


print(fib(chislo))
print("РЕКУРСИЯ:", N)


posled = [1] + [0] * (chislo)
for i in range(1, len(posled)):
    posled[i] = posled[i - 1] + posled[i - 2]
posled.pop(0)
posled.pop(0)
print("ДИНАМИКА:", posled[len(posled)-1])


predpredidush = 0
predidush = 1
sledush = 1
P = [1]
for i in range(chislo):
    sledush = predidush + predpredidush
    predidush, predpredidush = sledush, predidush
    P.append(predidush)
print("В ЛОБ:   ", P)
