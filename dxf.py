import sys
import dxfgrabber as dg
import turtle as tut

from numpy import pi,cos,sin,arctan2,sqrt

fname=('/test.dxf')
dxf=dg.readfile(fname)
print(dxf.header)

def tut_dxfline(l):
    x0=l.start[0]
    y0=l.start[1]
    x1=l.end[0]
    y1=l.end[1]
    deg = arctan2(y1-y0,x1-x0) / pi*180
    dist = sqrt((x1-x0)**2+(y1-y0)**2)

    tut.penup()
    tut.setpos(x0,y0)
    tut.setheading(deg)
    tut.pendown()
    tut.forward(dist)

def tut_dxfarc(a):
    deg0=a.start_angle
    deg1=a.end_angle
    r=a.radius
    x0=a.center[0]
    y0=a.center[1]
    if deg0 > deg1:
        deg0 = deg0-360

    tut.penup()
    tut.setpos(x0+r*cos(deg0/180.*pi),y0+r*sin(deg0/180.*pi))
    tut.setheading(deg0+90)
    tut.pendown()
    tut.circle(r,extent=(deg1-deg0))

def tut_dxfcir(c):
    r=c.radius
    x0=c.center[0]
    y0=c.center[1]

    tut.penup()
    tut.setpos(x0+r,y0)
    tut.setheading(90)
    tut.pendown()
    tut.circle(r)

#tut.speed("fastest")
tut.speed("fast")

for entity in dxf.entities:
    if entity.dxftype == 'LINE':
        tut_dxfline(entity)
    elif entity.dxftype == 'CIRCLE':
        tut_dxfcir(entity)
    elif entity.dxftype == 'ARC':
        tut_dxfarc(entity)
    else:
        print(entity.dxftype)

print("Draw End")            
tut.mainloop()