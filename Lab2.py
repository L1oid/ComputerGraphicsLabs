from tkinter import *
import math

root = Tk()
c = Canvas(root, width=640, height=480, bg='white')
c.pack()

angle = math.pi / 4

x1 = 185
y1 = 150

x2 = 125
y2 = 250

x3 = 250
y3 = 250

xMiddle = (x1 + x2 + x3) / 3
yMiddle = (y1 + y2 + y3) / 3


def show_triangle():
    c.create_line(xMiddle, yMiddle, xMiddle, yMiddle)
    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)


def right_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    xTemp = x1
    yTemp = y1
    x1 = xMiddle + (xTemp - xMiddle) * math.cos(angle) - (yTemp - yMiddle) * math.sin(angle)
    y1 = yMiddle + (xTemp - xMiddle) * math.sin(angle) + (yTemp - yMiddle) * math.cos(angle)

    xTemp = x2
    yTemp = y2
    x2 = xMiddle + (xTemp - xMiddle) * math.cos(angle) - (yTemp - yMiddle) * math.sin(angle)
    y2 = yMiddle + (xTemp - xMiddle) * math.sin(angle) + (yTemp - yMiddle) * math.cos(angle)

    xTemp = x3
    yTemp = y3
    x3 = xMiddle + (xTemp - xMiddle) * math.cos(angle) - (yTemp - yMiddle) * math.sin(angle)
    y3 = yMiddle + (xTemp - xMiddle) * math.sin(angle) + (yTemp - yMiddle) * math.cos(angle)

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)


def left_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    xTemp = x1
    yTemp = y1
    x1 = xMiddle + (xTemp - xMiddle) * math.cos(-angle) - (yTemp - yMiddle) * math.sin(-angle)
    y1 = yMiddle + (xTemp - xMiddle) * math.sin(-angle) + (yTemp - yMiddle) * math.cos(-angle)

    xTemp = x2
    yTemp = y2
    x2 = xMiddle + (xTemp - xMiddle) * math.cos(-angle) - (yTemp - yMiddle) * math.sin(-angle)
    y2 = yMiddle + (xTemp - xMiddle) * math.sin(-angle) + (yTemp - yMiddle) * math.cos(-angle)

    xTemp = x3
    yTemp = y3
    x3 = xMiddle + (xTemp - xMiddle) * math.cos(-angle) - (yTemp - yMiddle) * math.sin(-angle)
    y3 = yMiddle + (xTemp - xMiddle) * math.sin(-angle) + (yTemp - yMiddle) * math.cos(-angle)

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

def hide_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')


btnShowTriangle = Button(c, width=6, text="+", command=show_triangle)
btnShowTriangle.pack()
btnHideTriangle = Button(c, width=6, text="-", command=hide_triangle)
btnHideTriangle.pack()
btnRightTriangle = Button(c, width=6, text="->", command=right_triangle)
btnRightTriangle.pack()
btnLeftTriangle = Button(c, width=6, text="<-", command=left_triangle)
btnLeftTriangle.pack()

c.create_window((1, 1), anchor="nw", window=btnShowTriangle)
c.create_window((1, 31), anchor="nw", window=btnHideTriangle)
c.create_window((1, 61), anchor="nw", window=btnRightTriangle)
c.create_window((1, 91), anchor="nw", window=btnLeftTriangle)

root.mainloop()
