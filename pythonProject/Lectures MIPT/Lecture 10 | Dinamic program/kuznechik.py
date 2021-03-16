x = int(input("Введи количество клеток:"))
razreshenie = [True] * x
zapret1 = int(input("Запрещенная клетка 1:"))
zapret2 = int(input("Запрещенная клетка 2:"))
zapret3 = int(input("Запрещенная клетка 3:"))
razreshenie[zapret1] = False
razreshenie[zapret2] = False
razreshenie[zapret3] = False


def count_trajectories(n, allowed: list):       #N - номер клетки в массиве
    K = [0, 1, int(allowed[2])] + [0] * (n - 3) #создаю массив колличеств траекторий
    for i in range(3, n):
        if allowed[i]:
            K[i] = K[i - 1] + K[i - 2] + K[i - 3]
    print(K)


count_trajectories(x, razreshenie)
