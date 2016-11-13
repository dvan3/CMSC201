#Filename:    lab8.py
#Written by:  Dave Van
#Date:        4/5/10

from graphics import *

def main():

    win = GraphWin("MyPaint", 400, 400)

    done = False

    prompt = Text(Point(200, 360),"Color Fill")
    prompt.draw(win)

    prompt2 = Text(Point(200, 320),"Color Outline")
    prompt2.draw(win)

    color2 = Entry(Point(200, 340), 30)
    color2.draw(win)

    color = Entry(Point(200, 380), 30)
    color.draw(win)

    while not done:
        p1 = win.getMouse()
        p2 = win.getMouse()

        dx = p2.getX() - p1.getX()
        dy = p2.getY() - p1.getY()

        radius = (dx * dx + dy * dy) ** .5

        colorStr = color.getText().strip()

        colorStr2 = color2.getText().strip()

        circ = Circle(p1, radius)
        circ.setOutline(colorStr2)
        circ.setFill(colorStr)
        circ.draw(win)

        done = (dx == 0 and dy == 0)
    
    

main()
