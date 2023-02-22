from tkinter import *
import math

root = Tk()
c = Canvas(root, width=640, height=480, bg='white')
c.pack()

topX = 150
topY = 100
botX = 350
botY = 300

c.create_rectangle(topX, topY, botX, botY)

x1 = 185
y1 = 150

x2 = 125
y2 = 250

x3 = 250
y3 = 250

c.create_line(x1, y1, x2, y2)
c.create_line(x2, y2, x3, y3)
c.create_line(x3, y3, x1, y1)


def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    n = 0
    if y2 - y1 != 0:
        q = (x2 - x1) / (y1 - y2)
        sn = (x3 - x4) + (y3 - y4) * q
        if sn <= 0:
            return 0, 0
        fn = (x3 - x1) + (y3 - y1) * q
        n = fn / sn
    else:
        if y3 - y4 <= 0:
            return 0, 0
        n = (y3 - y1) / (y3 - y4)
    xcross = x3 + (x4 - x3) * n
    ycross = y3 + (y4 - y3) * n
    return xcross, ycross

def up_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    y1 -= 5
    y2 -= 5
    y3 -= 5


    if y1 <= topY or x2 <= topX:
        x1new, y1new = cross(x1, y1, x2, y2, topX, topY, botX, topY)
        if x1new == 0 and y1new == 0:
            x1new = x1
            y1new = y1
        x1new2, y1new2 = cross(x3, y3, x1, y1, topX, topY, botX, topY)
        if x1new2 == 0 and y1new2 == 0:
            x1new2 = x1
            y1new2 = y1
        x2new, y2new = cross(x1, y1, x2, y2, topX, topY, topX, botY)
        if x2new == 0 and y2new == 0:
            x2new = x2
            y2new = y2
        x2new2, y2new2 = cross(x2, y2, x3, y3, topX, topY, topX, botY)
        if x2new2 == 0 and y2new2 == 0:
            x2new2 = x2
            y2new2 = y2
        c.create_line(x1new, y1new, x2new, y2new)
        c.create_line(x2new2, y2new2, x3, y3)
        c.create_line(x3, y3, x1new2, y1new2)
    else:
        c.create_line(x1, y1, x2, y2)
        c.create_line(x2, y2, x3, y3)
        c.create_line(x3, y3, x1, y1)

    c.create_rectangle(150, 100, 350, 300)


def down_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    y1 += 5
    y2 += 5
    y3 += 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    c.create_rectangle(150, 100, 350, 300)


def right_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    x1 += 5
    x2 += 5
    x3 += 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    c.create_rectangle(150, 100, 350, 300)


def left_triangle():
    global x1, y1, x2, y2, x3, y3
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    x1 -= 5
    x2 -= 5
    x3 -= 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    c.create_rectangle(150, 100, 350, 300)


btnShowTriangle = Button(c, width=6, text="Up", command=up_triangle)
btnShowTriangle.pack()
btnHideTriangle = Button(c, width=6, text="Down", command=down_triangle)
btnHideTriangle.pack()
btnRightTriangle = Button(c, width=6, text="Right", command=right_triangle)
btnRightTriangle.pack()
btnLeftTriangle = Button(c, width=6, text="Left", command=left_triangle)
btnLeftTriangle.pack()

c.create_window((1, 1), anchor="nw", window=btnShowTriangle)
c.create_window((1, 31), anchor="nw", window=btnHideTriangle)
c.create_window((1, 61), anchor="nw", window=btnRightTriangle)
c.create_window((1, 91), anchor="nw", window=btnLeftTriangle)

root.mainloop()
