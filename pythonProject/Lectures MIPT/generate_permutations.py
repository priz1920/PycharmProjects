def find(number, A):
    """Ищет number в A и возвращает True, если такой есть
    False, если такого нет"""
    for x in A:
        if number == x:
            return True
    return False

def find2(number,A):
    """Ищет number в A и возвращает True, если такой есть
    False, если такого нет
    Однопроходный алгоритм с Флагом"""
    flag = False
    for x in A:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(N:int, M:int=-1, prefix=None):
    """ Генерация всех перестановок N чисел в M позициях,
    с префиксом prefix"""
    #if M == -1:
    #    M = N
    M = N if M == -1 else M  #по умолчанию N чисел в N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, end=", ", sep="")
        return
    for number in range(1, N+1):
        if find2(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(N, M-1, prefix)
        prefix.pop()

generate_permutations(2)