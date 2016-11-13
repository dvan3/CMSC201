#Filename:     lab7.py
#Written by:   Dave Van
#Date:         3/29/10

from graphics import *
from time import sleep

FRAMES = 100

def main():
    win = GraphWin("Lab 7", 400, 400)

    win.setBackground("orange")

    circ = Circle(Point(200, 200), 40)
    circ.setFill("white")
    circ.draw(win)

    circ2 = Circle(Point(200,130), 30)
    circ2.setFill("white")
    circ2.draw(win)

    circ3 = Circle(Point(200,300), 60)
    circ3.setFill("white")
    circ3.draw(win)

    prompt = Text(Point(200, 380),
                  "Click mouse on new location for circle")

    prompt.setTextColor("blue")
    prompt.draw(win)

    for i in range(3):
        new_location = win.getMouse()
        
        center = circ.getCenter()

        dx = float(new_location.getX() - center.getX()) / FRAMES
        dy = float(new_location.getY() - center.getY()) / FRAMES      

        for j in range(FRAMES):
            circ.move(dx, dy)
            circ2.move(dx, dy)
            circ3.move(dx, dy)
            sleep(1.0 / FRAMES)
    
main()
