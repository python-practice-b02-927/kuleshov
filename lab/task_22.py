#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_10():

    c1 = 1
    while not wall_is_on_the_right():
         c1 += 1
         move_right() 
    move_left(c1-1)
    
    c2 = 1
    while not wall_is_beneath():
         c2 += 1
         move_down() 
    move_up(c2-1)
    
    for i in range(c2):
        for j in range(c1-1):
            fill_cell()
            move_right()
        fill_cell()
        if not wall_is_beneath():
            move_down()
        move_left(n=c1-1)    
 

if __name__ == '__main__':
    run_tasks()
