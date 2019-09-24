import graphics as gr

SIZE_X = 800
SIZE_Y = 800
window = gr.GraphWin("Model", SIZE_X, SIZE_Y)


def tree(x1, y1, x2, y2):
    dx = x2-x1
    dy = y2 - y1

    trunk = gr.Rectangle(gr.Point(x1 + dx * (1 / 2 - 1 / 20), y1 + dy / 2), gr.Point(x1 + dx * (1 / 2 + 1 / 30), y2))
    trunk.setFill('lightblue')
    trunk.setOutline('lightblue')
    trunk.draw(window)

    leafs = gr.Oval(gr.Point(x1 + dx * (1 / 2 - 7 / 24), y1), gr.Point(x1 + dx * (1 / 2 + 7 / 24), y1 + dy * 5 / 12))
    leafs.setFill('darkgreen')
    leafs.setOutline('darkgreen')
    leafs.draw(window)

    leafs = gr.Oval(gr.Point(x1, y1 + dy / 4), gr.Point(x2, y1 + dy * (1 / 2 + 1 / 8)))
    leafs.setFill('darkgreen')
    leafs.setOutline('darkgreen')
    leafs.draw(window)

    leafs = gr.Oval(gr.Point(x1 + dx * (1 / 2 - 7 / 24), y1 + dy * (1 / 2 + 1 / 16)), gr.Point(x1 + dx * (1 / 2 + 7 / 24), y1 + dy * 4 / 5))
    leafs.setFill('darkgreen')
    leafs.setOutline('darkgreen')
    leafs.draw(window)

    fruit = gr.Oval(gr.Point(x1 + dx * 13 / 24, y1 + dy * 3 / 36), gr.Point(x1 + dx * 17 / 24, y1 + dy * 6 / 36))
    fruit.setFill('yellow')
    fruit.setOutline('yellow')
    fruit.draw(window)

    fruit = gr.Oval(gr.Point(x1 + dx * 19 / 24, y1 + dy * 15 / 36), gr.Point(x1 + dx * 23 / 24, y1 + dy * 18 / 36))
    fruit.setFill('yellow')
    fruit.setOutline('yellow')
    fruit.draw(window)

    fruit = gr.Oval(gr.Point(x1 + dx * 1 / 24, y1 + dy * 15 / 36), gr.Point(x1 + dx * 5 / 24, y1 + dy * 18 / 36))
    fruit.setFill('yellow')
    fruit.setOutline('yellow')
    fruit.draw(window)

    fruit = gr.Oval(gr.Point(x1 + dx * 1 / 24, y1 + dy * 15 / 36), gr.Point(x1 + dx * 5 / 24, y1 + dy * 18 / 36))
    fruit.setFill('yellow')
    fruit.setOutline('yellow')
    fruit.draw(window)



def main():
    tree(100, 100, 300, 500)


main()

window.getMouse()

window.close()

