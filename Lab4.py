from tkinter import *


def set_pixel(x, y):
    c.create_oval(x, y, x, y, width=0, fill='black')


def set_pixel4(cx, cy, r):
    set_pixel(cx, cy + r)
    set_pixel(cx, cy - r)
    set_pixel(cx + r, cy)
    set_pixel(cx - r, cy)


def set_pixel8(cx, cy, x, y):
    set_pixel(cx + x, cy + y)
    set_pixel(cx - x, cy + y)
    set_pixel(cx + x, cy - y)
    set_pixel(cx - x, cy - y)
    set_pixel(cx + y, cy + x)
    set_pixel(cx - y, cy + x)
    set_pixel(cx + y, cy - x)
    set_pixel(cx - y, cy - x)


def raster_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    e = 2 * dy - dx
    incr_e = 2 * dy
    incr_ne = 2 * dy - 2 * dx

    x = x1
    y = y1
    set_pixel(x, y)
    count = dx
    while count > 0:
        count = count - 1
        if e > 0:
            y = y + 1
            e = e + incr_ne
        else:
            e = e + incr_e
        x = x + 1
        set_pixel(x, y)


def raster_circle(cx, cy, r):
    x = 0
    y = r
    f = 1 - r
    incr_e = 3
    incr_se = 5 - 2 * r

    set_pixel4(cx, cy, r)
    while x <= y:
        if f > 0:
            y = y - 1
            f = f + incr_se
            incr_se = incr_se + 4
        else:
            f = f + incr_e
            incr_se = incr_se + 2
        incr_e = incr_e + 2
        x = x + 1
        set_pixel8(cx, cy, x, y)


root = Tk()
c = Canvas(root, width=640, height=480, bg='white')
c.pack()

x1 = 100
y1 = 100
x2 = 200
y2 = 200

raster_line(x1, y1, x2, y2)
raster_circle(300, 300, 200)

root.mainloop()
