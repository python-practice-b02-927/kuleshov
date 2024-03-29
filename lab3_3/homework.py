from tkinter import *
from random import randrange as rnd, choice
import time
import json

root = Tk()
root.geometry('900x700')
q = 3
balls = []

width = 800
height = 600

l = Label(root, bg='black', fg='white', width=20, font=('Courier', 44))
canv = Canvas(root, width=800, height=600, bg='white')
b = Button(root, text="Сохранить результат")

l.pack()
canv.pack(fill=BOTH)
b.pack()
l['text'] = 'Score: 0'


colors = ['red', 'orange', 'yellow', 'green', 'blue']
count = 0


def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x, point_1.y + point_2.y)
    return new_point


def new_balls():
    global balls

    for i in range(q):
        x = rnd(100, 700)
        y = rnd(100, 500)
        r = rnd(30, 50)
        ball = canv.create_oval(x-r, y-r, x+r, y+r, fill=choice(colors), width=0)
        velocity = [rnd(1, 10), rnd(1, 10)]
        balls.append([ball, velocity])

    root.after(2000, new_balls)


def getxyr(ball):
    global x, y, r
    pos = canv.coords(ball)
    r = (pos[2] - pos[0]) / 2
    x = pos[0] + r
    y = pos[1] + r


def move_balls():
    global x, y, r

    for i in balls:
        getxyr(i[0])
        vel = i[1]
        if (vel[0] > 0) and (x + r + vel[0]) > width:
            vel[0] *= -1
        if (vel[0] < 0) and (x - r + vel[0]) < 0:
            vel[0] *= -1

        dy = (-1)**rnd(1, 2)
        if (vel[1] > 0) and (y + r + vel[1]) > height:
            vel[1] *= -1
        if (vel[1] < 0) and (y - r + vel[1]) < 0:
            vel[1] *= -1

        canv.coords(i[0], x - r + vel[0], y - r + vel[1], x + r + vel[0], y + r + vel[1])
    root.after(50, move_balls)


def click(event):
    global count, x, y, r
    for i in balls:
        ball = i[0]
        getxyr(ball)
        if (event.x - x)**2 + (event.y - y)**2 <= r**2:
            count += 1
            canv.delete(ball)
            balls.remove(i)
        l['text'] = 'Score: ' + str(count)


def save(event):
    global count, leaderboard
    if (len(leaderboard) < 10) or (count > min(leaderboard)):
        leaderboard.append(count)
        leaderboard.sort(reverse=True)
        leaderboard = leaderboard[:10]
        with open('leaderboard.json', 'w') as f:
            lst1 = [[j + 1, leaderboard[j]] for j in range(len(leaderboard))]
            json.dump(lst1, f, indent=2)


leaderboard = []
try:
    file = open('leaderboard.json', 'r')
except:
    pass
else:
    try:
        lst = json.load(file)
    except:
        pass
    else:
        leaderboard = [lst[i][1] for i in range(len(lst))]
    file.close()
    print(leaderboard)

new_balls()
move_balls()
canv.bind('<Button-1>', click)
b.bind('<Button-1>', save)
mainloop()
