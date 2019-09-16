#!/usr/bin/python3

from pyrob.api import *

def cross():
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
@task
def task_2_1():
    
    move_right(n=2)
    move_down()
    cross()
    move_left()


if __name__ == '__main__':
    run_tasks()
