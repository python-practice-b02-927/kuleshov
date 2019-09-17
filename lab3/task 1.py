import graphics as gr
import random

w = 800
h = 600


def cloud(w1, h1, r):
    circle1 = gr.Circle(gr.Point(w1, h1), r)
    circle2 = gr.Circle(gr.Point(w1 + r, h1), r)
    circle3 = gr.Circle(gr.Point(w1 + 3 * r / 2, h1 + r / 2), r)
    circle4 = gr.Circle(gr.Point(w1 + r / 2, h1 + r / 2), r)
    circle5 = gr.Circle(gr.Point(w1 - r / 2, h1 + r / 2), r)
    circle1.setFill('white')
    circle2.setFill('white')
    circle3.setFill('white')
    circle4.setFill('white')
    circle5.setFill('white')
    circle1.draw(window)
    circle2.draw(window)
    circle3.draw(window)
    circle4.draw(window)
    circle5.draw(window)


def wheel(cx, cy, r1, r2):
    circle1 = gr.Circle(gr.Point(cx, cy), r2)
    circle1.setFill('black')
    circle2 = gr.Circle(gr.Point(cx, cy), r1)
    circle2.setFill('gray')
    circle1.draw(window)
    circle2.draw(window)



window = gr.GraphWin("Jenkslex and Ganzz project", w, h)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(w, h/2))
sky.setFill('blue')

ground = gr.Rectangle(gr.Point(0, h/2), gr.Point(w, h))
ground.setFill('green')

sky.draw(window)
ground.draw(window)

sun = gr.Circle(gr.Point(700, 50), 40)
sun.setFill('yellow')
sun.draw(window)

cloudx1 = 100
cloudy1 = 20
cloud_distance = 30
n = 8

for i in range(1, n):
    cloud(cloudx1 * i, cloudy1 + random.randint(1, 600) / 100 * cloud_distance, 20)

corp = gr.Polygon(gr.Point(290, 490), gr.Point(290, 405), gr.Point(340, 405), gr.Point(350, 445), gr.Point(405, 445), gr.Point(405, 490), gr.Point(300, 490))
corp.setFill('red')
corp.draw(window)

wind = gr.Polygon(gr.Point(295, 445), gr.Point(295, 410), gr.Point(335, 410), gr.Point(343.75, 445), gr.Point(295, 445))
wind.setFill('green')
wind.draw(window)

line1 = gr.Line(gr.Point(295, 445), gr.Point(295, 490))
line1.setFill('black')
line1.draw(window)

line2 = gr.Line(gr.Point(343.75, 445), gr.Point(343.75, 490))
line2.setFill('black')
line2.draw(window)

handle = gr.Rectangle(gr.Point(330, 450), gr.Point(340, 453))
handle.setFill('black')
handle.draw(window)

wheel(300, 485, 20, 30)
wheel(400, 500, 10, 15)

tree = gr.Rectangle(gr.Point(700, 250), gr.Point(720, 450))
tree.setFill('brown')
tree.draw(window)

leaflayer1 = gr.Polygon(gr.Point(650, 400), gr.Point(710, 320), gr.Point(770, 400))
leaflayer1.setFill('darkgreen')
leaflayer1.draw(window)

leaflayer2 = gr.Polygon(gr.Point(670, 350), gr.Point(710, 270), gr.Point(750, 350))
leaflayer2.setFill('darkgreen')
leaflayer2.draw(window)

leaflayer3 = gr.Polygon(gr.Point(675, 320), gr.Point(710, 220), gr.Point(745, 320))
leaflayer3.setFill('darkgreen')
leaflayer3.draw(window)

house = gr.Rectangle(gr.Point(20, 250), gr.Point(120, 350))
house.setFill('gray')
house.draw(window)

roof = gr.Polygon(gr.Point(20, 250), gr.Point(70, 200), gr.Point(120, 250))
roof.setFill('brown')
roof.draw(window)

wind1 = gr.Rectangle(gr.Point(50, 280), gr.Point(90, 320))
wind1.setFill('yellow')
wind1.draw(window)

wline1 = gr.Line(gr.Point(70, 280), gr.Point(70, 320))
wline1.setWidth(3)
wline1.draw(window)

wline2 = gr.Line(gr.Point(50, 300), gr.Point(90, 300))
wline2.setWidth(3)
wline2.draw(window)

window.getMouse()

window.close()