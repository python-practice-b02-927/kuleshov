from tkinter import *

root = Tk()

root.geometry('600x400+200+100')

e = Entry(root, width=20)
b = Button(root, text="Преобразовать")
l = Label(root, bg='black', fg='white', width=20)


def strToSortlist(event):
    s = e.get()
    s = s.split()
    s.sort()
    l['text'] = ' '.join(s)


b.bind('<Button-1>', strToSortlist)

e.pack()
b.pack()
l.pack()

root.mainloop()