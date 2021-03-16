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
def task_2_1():
    move_down()
    move_right()
    cross()




if __name__ == '__main__':
    run_tasks()
