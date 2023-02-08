from tkinter import *

root = Tk()
c = Canvas(root, width=640, height=480, bg='white')
c.pack()

globalRectangle = 0
globalTriangle = 0
globalOval = 0


def show_rectangle():
    c.create_rectangle(150, 100, 250, 200)
    global globalRectangle
    globalRectangle = 1


def hide_rectangle():
    c.create_rectangle(150, 100, 250, 200, outline='white')
    global globalRectangle
    globalRectangle = 0
    if globalTriangle == 1:
        c.create_line(185, 150, 125, 250)
        c.create_line(250, 250, 185, 150)
    if globalOval == 1:
        show_oval()


def show_triangle():
    c.create_line(185, 150, 125, 250)
    c.create_line(125, 250, 250, 250)
    c.create_line(250, 250, 185, 150)
    global globalTriangle
    globalTriangle = 1


def hide_triangle():
    c.create_line(185, 150, 125, 250, fill='white')
    c.create_line(125, 250, 250, 250, fill='white')
    c.create_line(250, 250, 185, 150, fill='white')
    global globalTriangle
    globalTriangle = 0
    if globalRectangle == 1:
        c.create_line(150, 200, 250, 200)
    if globalOval == 1:
        show_oval()


def show_oval():
    c.create_oval(200, 160, 290, 240)
    global globalOval
    globalOval = 1


def hide_oval():
    c.create_oval(200, 160, 290, 240, outline='white')
    global globalOval
    globalOval = 0
    if globalRectangle == 1:
        c.create_line(150, 200, 250, 200)
        c.create_line(250, 100, 250, 200)
    if globalTriangle == 1:
        c.create_line(250, 250, 185, 150)


btnShowRectangle = Button(c, width=6, text="+", command=show_rectangle)
btnShowRectangle.pack()
btnHideRectangle = Button(c, width=6, text="-", command=hide_rectangle)
btnHideRectangle.pack()

c.create_rectangle(15, 5, 40, 25)
c.create_window((1, 30), anchor="nw", window=btnShowRectangle)
c.create_window((1, 60), anchor="nw", window=btnHideRectangle)

btnShowTriangle = Button(c, width=6, text="+", command=show_triangle)
btnShowTriangle.pack()
btnHideTriangle = Button(c, width=6, text="-", command=hide_triangle)
btnHideTriangle.pack()
btnRightTriangle = Button(c, width=6, text="->")
btnRightTriangle.pack()
btnLeftTriangle = Button(c, width=6, text="<-")
btnLeftTriangle.pack()

c.create_polygon(85, 5, 75, 25, 95, 25, fill='white', outline='black')
c.create_window((60, 30), anchor="nw", window=btnShowTriangle)
c.create_window((60, 60), anchor="nw", window=btnHideTriangle)
c.create_window((60, 90), anchor="nw", window=btnRightTriangle)
c.create_window((60, 120), anchor="nw", window=btnLeftTriangle)

btnShowOval = Button(c, width=6, text="+", command=show_oval)
btnShowOval.pack()
btnHideOval = Button(c, width=6, text="-", command=hide_oval)
btnHideOval.pack()

c.create_oval(135, 5, 160, 25)
c.create_window((120, 30), anchor="nw", window=btnShowOval)
c.create_window((120, 60), anchor="nw", window=btnHideOval)

root.mainloop()
