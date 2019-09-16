#!/usr/bin/python3

from pyrob.api import *


def up_and_back():
    if not wall_is_above():
        c = 0
        while not wall_is_above():
            move_up()
            fill_cell()
            c += 1
        move_down(n=c)


@task(delay=0.01)
def task_6_6():

    move_right()
    while not wall_is_on_the_right():
        up_and_back()
        move_right()
    up_and_back()
    while wall_is_beneath():
        move_left()


if __name__ == '__main__':
    run_tasks()
