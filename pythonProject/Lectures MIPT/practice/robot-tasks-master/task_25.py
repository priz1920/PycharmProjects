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

@task
def task_2_2():
    move_down()
    cross()
    for i in range(4):
        move_right(4)
        cross()


if __name__ == '__main__':
    run_tasks()
