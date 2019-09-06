#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():

    c = 0
    while not wall_is_on_the_right():
        if cell_is_filled():
            c += 1
        if wall_is_above():
            fill_cell()
        else:
            move_up()
            c1 = 0
            while not wall_is_above():
                if cell_is_filled():
                    c += 1
                else:
                    fill_cell()
                move_up()
                c1 += 1
            if cell_is_filled():
                c += 1
            else:
                fill_cell()
            move_down(c1 + 1)
        move_right()

    mov('ax', c)


if __name__ == '__main__':
    run_tasks()
