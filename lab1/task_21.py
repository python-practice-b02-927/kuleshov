#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    
    move_right()
    move_down()
    for i in range(13):
        for j in range(i):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        if i > 0:
            move_left(n=i)
	 
if __name__ == '__main__':
    run_tasks()
