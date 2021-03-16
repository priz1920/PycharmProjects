#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    n = 0
    move_right()
    fill_cell()
    while not wall_is_on_the_right():

        fill_cell()
        for i in range(n):
            if wall_is_on_the_right():
                break
            move_right()
        n += 1




if __name__ == '__main__':
    run_tasks()
