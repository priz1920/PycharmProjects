#!/usr/bin/python3

from pyrob.api import *
def cross():
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_left()

@task(delay=0.02)
def task_2_4():
    for k in range(4):
        cross()
        for i in range(9):
            move_right(4)
            cross()
        move_left(36)
        move_down(4)
    cross()
    for i in range(9):
        move_right(4)
        cross()
    move_left(36)


if __name__ == '__main__':
    run_tasks()
