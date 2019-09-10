#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():

    move_right()
    while not wall_is_on_the_right():
        if not wall_is_above():
            c = 0
            while not wall_is_above():
                move_up()
                fill_cell()
                c += 1
            move_down(n=c)
        move_right()
    if not wall_is_above():
        c = 0
        while not wall_is_above():
            move_up()
            fill_cell()
            c += 1
        move_down(n=c)       
    while wall_is_beneath():
        move_left()

if __name__ == '__main__':
    run_tasks()
