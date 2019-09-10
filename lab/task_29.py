#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    
    a = 0
    c = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            if a == 1:
                c += 1
            else:
                c = 1
            a = 1
        else:
            a = 0
        if c == 3:
            break
        move_right()



if __name__ == '__main__':
    run_tasks()
