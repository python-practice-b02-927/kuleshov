#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():

    move_right()
    a = 1
    i = 1
    while a == 1:
        fill_cell()
        for j in range(i):
            if not wall_is_on_the_right():
                move_right()
            else:
                a = 0
                break
        i += 1


if __name__ == '__main__':
    run_tasks()
