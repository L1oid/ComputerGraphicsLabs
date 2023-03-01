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

x1new = x1
y1new = y1
x1new2 = x1
y1new2 = y1
x2new = x2
y2new = y2
x2new2 = x2
y2new2 = y2
x3new = x3
y3new = y3

c.create_line(x1, y1, x2, y2)
c.create_line(x2, y2, x3, y3)
c.create_line(x3, y3, x1, y1)

def cross(x1, y1, x2, y2, x3, y3, x4, y4):
    if y2 - y1 != 0:
        q = (x2 - x1) / (y1 - y2)
        sn = (x3 - x4) + (y3 - y4) * q
        fn = (x3 - x1) + (y3 - y1) * q
        n = fn / sn
    else:
        n = (y3 - y1) / (y3 - y4)
    xcross = x3 + (x4 - x3) * n
    ycross = y3 + (y4 - y3) * n
    return xcross, ycross

def up_triangle():
    global x1, y1, x2, y2, x3, y3
    global x1new, y1new, x1new2, y1new2, x2new, y2new, x2new2, y2new2, x3new, y3new

    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    c.create_line(x1new, y1new, x2new, y2new, fill='white')
    c.create_line(x2new, y2new, x3new, y3new, fill='white')
    c.create_line(x3new, y3new, x1new2, y1new2, fill='white')

    y1 -= 5
    y2 -= 5
    y3 -= 5

    if y1 <= topY:
        print("Есть пересечения")
        x1new, y1new = cross(x1, y1, x2, y2, topX, topY, botX, topY)
        x1new2, y1new2 = cross(x3, y3, x1, y1, topX, topY, botX, topY)
        if y2 <= topY:
            print("klol")
            x1new = topX
            y1new = topY
            x1new2 = topX
            y1new2 = topY
            x2new = topX
            y2new = topY
            x3new = topX
            y3new = topY
        else:
            print("debil")
            x2new = x2
            y2new = y2
            x3new = x3
            y3new = y3
        c.create_line(x1new, y1new, x2new, y2new)
        c.create_line(x2new, y2new, x3new, y3new)
        c.create_line(x3new, y3new, x1new2, y1new2)
    else:
        print("Нет пересечение")
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
