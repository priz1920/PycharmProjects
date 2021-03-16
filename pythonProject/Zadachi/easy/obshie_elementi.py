""" Выводит список состоящий из общих
    элементов двух заданных списков"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for elemA in a:
    for elemB in b:
        if elemA == elemB:
            c.append(elemA)
print(set(c))

result = list(filter(lambda elem: elem in b, a))
result2 = [elem for elem in a if elem in b]
result3 = list(set(a) & set(b))
print(result)
print(result2)
print(result3)








