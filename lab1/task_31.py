#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    a = True

    while a:
        while not wall_is_on_the_right():
            move_right()

        while not wall_is_on_the_left():
            if not wall_is_beneath():
                move_down()
                break
            move_left()

        if wall_is_on_the_left():
            if wall_is_beneath():
                a = False
            else:
                move_down()


if __name__ == '__main__':
    run_tasks()
