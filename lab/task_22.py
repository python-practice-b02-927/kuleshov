#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_10():

    x = 1
    while not wall_is_on_the_right():
        x += 1
        move_right()
    if x > 1:
        move_left(n=x-1)

    y = 1
    while not wall_is_beneath():
        y += 1
        move_down()
    if y > 1:
        move_up(n=y-1)

    for i in range(y):
        for j in range(x - 1):
            fill_cell()
            move_right()
        fill_cell()
        if y > 1:
            move_left(n=x-1)
        if not wall_is_beneath():
            move_down()



if __name__ == '__main__':
    run_tasks()
