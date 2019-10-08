from tkinter import *
from random import randrange as rnd, choice
import time

root = Tk()
root.geometry('900x700')
q = 3
balls = []

l = Label(root, bg='black', fg='white', width=20, font=('Courier', 44))
canv = Canvas(root, width=800, height=600, bg='white')

l.pack()
canv.pack(fill=BOTH, expand=1)
l['text'] = 'Score: 0'


colors = ['red', 'orange', 'yellow', 'green', 'blue']
count = 0


def new_ball():
    global balls

    for i in range(q):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        ball = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
        balls.append(ball)

    root.after(2000, new_ball)


def click(event):
    global count, flag
    for ball in balls:
        pos = canv.coords(ball)
        r = (pos[2] - pos[0])/2
        x = pos[0] + r
        y = pos[1] + r
        if (event.x - x)**2 + (event.y - y)**2 <= r**2:
            count += 1
            canv.delete(ball)
            balls.remove(ball)
        l['text'] = 'Score: ' + str(count)


new_ball()
canv.bind('<Button-1>', click)
mainloop()
