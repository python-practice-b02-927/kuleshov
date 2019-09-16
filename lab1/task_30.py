#!/usr/bin/python3

from pyrob.api import *


def square(f):
    move_right()
    for i in range(f-2):
        fill_cell()
        move_right()
    move_down()
    for i in range(f-2):
        fill_cell()
        move_down()
    move_left()
    for i in range(f-2):
        fill_cell()
        move_left()
    move_up()
    for i in range(f-2):
        fill_cell()
        move_up()


@task(delay=0.01)
def task_9_3():

    x = 1
    while not wall_is_on_the_right():
        x += 1
        move_right()
    move_left(n=x-1)
    w = x
    
    while x >= 3:
        square(x)
        x -= 2
        move_right()
        move_down()
    move_left((w-1)//2)
    move_down((w-1)//2)
    

if __name__ == '__main__':
    run_tasks()
