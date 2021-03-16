#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    for i in range(100):
        #Бежим вниз пока не упремся
        while not wall_is_beneath():
            move_down()
        #Ищем выход
        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()
        if wall_is_beneath():
            while not wall_is_on_the_right() and wall_is_beneath():
                move_right()
            # Если выхода нет - завершаем цикл
            if wall_is_on_the_right() and wall_is_beneath():
                break
    # Бежим домой
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
