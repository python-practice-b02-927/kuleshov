#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    fill_cell()
    move_right(n=2)
    fill_cell()
    move_left()
    fill_cell()
    move_down()
    fill_cell()
    move_up(n=2)
    move_left()
@task
def task_2_2():
    
    move_down()
    for i in range(4):
        cross()
        move_right(4)
    cross()


if __name__ == '__main__':
    run_tasks()
