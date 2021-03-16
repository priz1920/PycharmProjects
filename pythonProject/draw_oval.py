from graphics import *
win = GraphWin("Окно для графики", 300, 300)
obj = Oval(Point(100, 100), Point(250, 200))
obj.draw(win)
win.getMouse()
win.close()