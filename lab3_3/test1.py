from tkinter import *

root = Tk()

root.geometry('600x400+200+100')

c = Canvas(root, width=300, height=300, bg='white')
c.pack()

c.create_line(10, 10, 190, 50)

c.create_line(100, 180, 100, 60, fill='green',
                width=5, arrow=LAST, dash=(10,2),
                activefill='lightgreen',
                arrowshape="10 20 10")

c.create_polygon(40, 110, 160, 110, 190, 180, 10, 180,
                fill='orange', outline='black', activefill='brown')

c.create_oval(50, 10, 150, 110, width=2)
c.create_oval(10, 120, 190, 190, fill='grey70', outline='white')

c.create_text(150, 150, text="WE LIVE IN A SOCIETY",
                justify=CENTER, font="Verdana 14")
c.create_text(300, 300, text="BOTTOM TEXT",
                anchor=SE, fill="yellow")

root.mainloop()