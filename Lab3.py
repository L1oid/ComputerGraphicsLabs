from tkinter import *

root = Tk()
c = Canvas(root, width=640, height=480, bg='white')
c.pack()

shift = 1

topX = 150
topY = 100
botX = 350
botY = 300

c.create_rectangle(topX, topY, botX, botY)

x1 = 215
y1 = 150

x2 = 155
y2 = 250

x3 = 280
y3 = 250

c.create_line(x1, y1, x2, y2)
c.create_line(x2, y2, x3, y3)
c.create_line(x3, y3, x1, y1)


def cross(shift):
    for i in range(1, shift):
        c.create_rectangle(topX - i, topY - i, botX + i, botY + i, outline='red')


def up_triangle():
    global x1, y1, x2, y2, x3, y3, shift
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    y1 -= 5
    y2 -= 5
    y3 -= 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    if y1 < topY or x2 < topX or x3 > botX or y2 > botY:
        print("Outline", shift)
        shift += 5
        cross(shift)

    if y1 > topY and x2 > topX and x3 < botX and y2 < botY:
        print("Reset", shift)
        shift = 1

    c.create_rectangle(150, 100, 350, 300)


def down_triangle():
    global x1, y1, x2, y2, x3, y3, shift
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    y1 += 5
    y2 += 5
    y3 += 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    if y1 < topY or x2 < topX or x3 > botX or y2 > botY:
        print("Outline", shift)
        shift += 5
        cross(shift)

    if y1 > topY and x2 > topX and x3 < botX and y2 < botY:
        print("Reset", shift)
        shift = 1

    c.create_rectangle(150, 100, 350, 300)


def right_triangle():
    global x1, y1, x2, y2, x3, y3, shift
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    x1 += 5
    x2 += 5
    x3 += 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    if y1 < topY or x2 < topX or x3 > botX or y2 > botY:
        print("Outline", shift)
        shift += 5
        cross(shift)

    if y1 > topY and x2 > topX and x3 < botX and y2 < botY:
        print("Reset", shift)
        shift = 1

    c.create_rectangle(150, 100, 350, 300)


def left_triangle():
    global x1, y1, x2, y2, x3, y3, shift
    c.create_line(x1, y1, x2, y2, fill='white')
    c.create_line(x2, y2, x3, y3, fill='white')
    c.create_line(x3, y3, x1, y1, fill='white')

    x1 -= 5
    x2 -= 5
    x3 -= 5

    c.create_line(x1, y1, x2, y2)
    c.create_line(x2, y2, x3, y3)
    c.create_line(x3, y3, x1, y1)

    if y1 < topY or x2 < topX or x3 > botX or y2 > botY:
        print("Outline", shift)
        shift += 5
        cross(shift)

    if y1 > topY and x2 > topX and x3 < botX and y2 < botY:
        print("Reset", shift)
        shift = 1

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
