#!/usr/bin/python3

from pyrob.api import *
import math

@task(delay=0.01)
def task_9_3():
    # Считаем высоту треугольников и размер поля
    global bok
    dl = 1
    while not wall_is_beneath():
        move_down()
        dl += 1
    move_up(dl-1)


    #цикл по количеству строк
    for k in range(dl):

        #цикл по каждой строке
        while not wall_is_on_the_right():

            #Вычисляем боковые клетки закрасить
            if k < dl/2:
                bok = k
            if k > (dl-1)/2:
                bok = (dl-1)-k

            # Закрашиваем слева
            if bok > 0:
                for x in range(bok):
                    fill_cell()
                    move_right()
            if bok != (dl-1)/2:
                move_right()

            # Определяем количество центаральных клеток
            if dl - 2*bok >= 3:
                centre = (dl - 2 * bok) - 2
            else:
                centre = 0

            # Закрашиваем центр
            if centre > 0:
                for y in range(centre):
                    fill_cell()
                    move_right()
            if not wall_is_on_the_right():
                move_right()

            # Закрашиваем правй бок
            if bok > 0:
                for x in range(bok):
                    fill_cell()
                    if not wall_is_on_the_right():
                        move_right()

        #Возвращаемся на финищ
        move_left(dl-1)
        if not wall_is_beneath():
            move_down()


if __name__ == '__main__':
    run_tasks()
