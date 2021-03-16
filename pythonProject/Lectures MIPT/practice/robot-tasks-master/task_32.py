#!/usr/bin/python3

from pyrob.api import *



@task(delay=0.01)
def task_8_18():
    i = 0
    while not wall_is_on_the_right():
        mov(i, i)

        move_right()
        i += 1
        if not wall_is_above():
            while not wall_is_above():
                move_up()

                fill_cell()
            while not wall_is_beneath():
                fill_cell()
                move_down()
    while not wall_is_on_the_left() and wall_is_beneath():
        move_left()


if __name__ == '__main__':
    run_tasks()
