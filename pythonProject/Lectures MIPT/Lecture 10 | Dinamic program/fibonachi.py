
n = int(input("Веди номер элемента в последовательности Фебоначи:"))

#С помощью рекурсии
"""
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("Число Фибоначи:", fib(n+2))
"""

#Динамическая функция
"""
fib = [0, 1]+[0]*(n-1)
for i in range(2, n+1):
    fib[i] = fib[i-1] + fib[i - 2]
print("Последовательность Фибоначи:", fib)
print("Число Фибоначи:", fib[n])
"""

#В лоб
"""
x = 0
y = 1
B = n
for k in range(B):
    n = x + y
    x = y
    y = n
print(x)
"""

#В лоб коротко
"""
a,b,n = 0, 1, n
for i in range(2, n+1):
    a,b = b, a+b
print(b)
"""