#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    b = 2
    move_right()
    move_down()
    fill_cell()
    for k in range(12):
        move_down()
        fill_cell()
        for i in range(1,b):
            move_right()
            fill_cell()
        b += 1
        move_left(b-2)
    move_down()

if __name__ == '__main__':
    run_tasks()
