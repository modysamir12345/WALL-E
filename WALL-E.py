from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def drawCircle(r=0.1, xc=0, yc=0):
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, 0.001):
        glColor3f(0, 0,0)

        x = r * cos(theta)
        y = r * sin(theta)

        glVertex(x + xc, y + yc)
    glEnd()

def draw():
    glClearColor(0.5,0,0.9,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)

    glColor3f(0.5, 0.5, 1)


    glBegin(GL_POLYGON)
    a = 0.7
    b = 0.3
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = a * cos(theta)
        y = b * sin(theta)
        glVertex(x, y-0.6)
    glEnd()



    glBegin(GL_LINES)
    glVertex(0,1)
    glVertex(0,-1)
    glVertex(1,0)
    glVertex(-1,0)
    glEnd()



    glColor3f(0.9,1,0)
    glBegin(GL_QUADS)
    glVertex(0.4, 0.4)
    glVertex(0.4, -0.4)
    glVertex(-0.4, -0.4)
    glVertex(-0.4, 0.4)

    glEnd()


    glColor3f(0.9, 1, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.1, 0.1)
    glVertex(0.1, -0.1)
    glVertex(-0.1, -0.1)
    glVertex(-0.1, 0.1)

    glEnd()

    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.4,0.2)
    glVertex(-0.4, 0.2)
    glVertex(-0.4,0.25)
    glVertex(0.4,0.25)

    glEnd()

    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.3, 0.25)
    glVertex(0.32, 0.25)
    glVertex(0.32, 0.4)
    glVertex(0.3, 0.4)

    glEnd()

    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.2, 0.25)
    glVertex(0.22, 0.25)
    glVertex(0.22, 0.4)
    glVertex(0.2, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.22, 0.35)
    glVertex(0.32, 0.35)
    glVertex(0.32, 0.37)
    glVertex(0.22, 0.37)

    glEnd()


    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(-0.22, 0.35)
    glVertex(-0.32, 0.35)
    glVertex(-0.32, 0.37)
    glVertex(-0.22, 0.37)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(0.4, 0.4)
    glVertex(0.4, -0.4)
    glVertex(-0.4, -0.4)
    glVertex(-0.4, 0.4)
    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(0.401, 0.401)
    glVertex(0.401, -0.401)
    glVertex(-0.401, -0.401)
    glVertex(-0.401, 0.401)
    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(-0.2, 0.25)
    glVertex(-0.22, 0.25)
    glVertex(-0.22, 0.4)
    glVertex(-0.2, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_QUADS)
    glVertex(-0.3, 0.25)
    glVertex(-0.32, 0.25)
    glVertex(-0.32, 0.4)
    glVertex(-0.3, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_POLYGON)
    r=0.05
    for theta in np.arange(0,2*pi,0.0001):
        x=r*cos(theta)
        y=r*sin(theta)
        glVertex(x+0.1,y+0.32)
    glEnd()

    glColor3f(1, 0, 0)
    glBegin(GL_POLYGON)
    r = 0.03
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x+0.1, y + 0.32)
    glEnd()

    glColor3f(0.9, 1, 0)
    glBegin(GL_QUADS)
    glVertex(0.4, 0.4)
    glVertex(0.5,0.3)
    glVertex(0.5,0.1)
    glVertex(0.4,0.1)
    glEnd()
    glColor3f(0,0 , 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(0.4, 0.4)
    glVertex(0.5, 0.3)
    glVertex(0.5, 0.1)
    glVertex(0.4, 0.1)
    glEnd()

    glColor3f(0.9, 1, 0)
    glBegin(GL_QUADS)
    glVertex(-0.4, 0.4)
    glVertex(-0.5, 0.3)
    glVertex(-0.5, 0.1)
    glVertex(-0.4, 0.1)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(-0.4, 0.4)
    glVertex(-0.5, 0.3)
    glVertex(-0.5, 0.1)
    glVertex(-0.4, 0.1)

    glEnd()

    glColor3f(0.5,0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex(0.5, 0)
    glVertex(0.3, 0)
    glVertex(0.1, 0.1)
    glVertex(0.4, 0.1)
    glVertex(0.4, 0.2)
    glVertex(0.1, 0.2)
    glVertex(0.3, 0.3)
    glVertex(0.5, 0.3)
    glEnd()
    glColor3f(0.9,1,0)
    glBegin(GL_POLYGON)
    glVertex(0.1, 0.1)
    glVertex(0.4, 0.1)
    glVertex(0.4, 0.2)
    glVertex(0.1, 0.2)

    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    glVertex(-0.5, 0)
    glVertex(-0.3, 0)
    glVertex(-0.1, 0.1)
    glVertex(-0.4, 0.1)
    glVertex(-0.4, 0.2)
    glVertex(-0.1, 0.2)
    glVertex(-0.3, 0.3)
    glVertex(-0.5, 0.3)
    glEnd()
    glColor3f(0.9, 1, 0)
    glBegin(GL_POLYGON)
    glVertex(-0.1, 0.1)
    glVertex(-0.4, 0.1)
    glVertex(-0.4, 0.2)
    glVertex(-0.1, 0.2)

    glEnd()
    glColor3f(0.9, 1, 0)
    glBegin(GL_QUADS)
    glVertex(0.1, 0.4)
    glVertex(0.1, 0.6)
    glVertex(-0.1, 0.6)
    glVertex(-0.1, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(0.1, 0.4)
    glVertex(0.1, 0.6)
    glVertex(-0.1, 0.6)
    glVertex(-0.1, 0.4)

    glEnd()
    glColor3f(0.9, 1, 0)
    glBegin(GL_QUADS)
    glVertex(0.05, 0.6)
    glVertex(0.05, 0.8)
    glVertex(-0.05, 0.8)
    glVertex(-0.05, 0.6)
    glEnd()

    glColor3f(0.9, 1, 0)
    glBegin(GL_POLYGON)
    a = 0.3
    b = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = a * cos(theta)
        y = b * sin(theta)
        glVertex(x, y + 0.8)
    glEnd()

    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    a = 0.3
    b = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = a * cos(theta)
        y = b * sin(theta)
        glVertex(x, y + 0.8)
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    r = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x + 0.2, y + 0.8)
    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_POLYGON)
    r = 0.1
    for theta in np.arange(0, 2 * pi, 0.0001):
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex(x - 0.2, y + 0.8)
    glEnd()
    drawCircle(0.05,0.2,0.8)
    drawCircle(0.05,-0.2,0.8)

    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex(0.4,-0.2)
    glVertex(0.6, -0.2)
    glVertex(0.6,-0.6)
    glVertex(0.4,-0.6)

    glEnd()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex(-0.4, -0.2)
    glVertex(-0.6, -0.2)
    glVertex(-0.6, -0.6)
    glVertex(-0.4, -0.6)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(0.4, -0.25)
    glVertex(0.6, -0.25)
    glVertex(0.6, -0.3)
    glVertex(0.4, -0.3)

    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(0.4, -0.35)
    glVertex(0.6, -0.35)
    glVertex(0.6, -0.4)
    glVertex(0.4, -0.4)

    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(0.4, -0.45)
    glVertex(0.6, -0.45)
    glVertex(0.6, -0.5)
    glVertex(0.4, -0.5)

    glEnd()

    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(0.4, -0.55)
    glVertex(0.6, -0.55)
    glVertex(0.6, -0.6)
    glVertex(0.4, -0.6)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.4, -0.25)
    glVertex(-0.6, -0.25)
    glVertex(-0.6, -0.3)
    glVertex(-0.4, -0.3)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.4, -0.35)
    glVertex(-0.6, -0.35)
    glVertex(-0.6, -0.4)
    glVertex(-0.4, -0.4)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.4, -0.45)
    glVertex(-0.6, -0.45)
    glVertex(-0.6, -0.5)
    glVertex(-0.4, -0.5)

    glEnd()
    glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-0.4, -0.55)
    glVertex(-0.6, -0.55)
    glVertex(-0.6, -0.6)
    glVertex(-0.4, -0.6)

    glEnd()
    glColor3f(0.9, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex(0.1, 0.6)
    glVertex(0.2, 0.4)
    glVertex(0.1, 0.4)

    glEnd()
    glColor3f(0.9, 1, 0)
    glBegin(GL_TRIANGLES)
    glVertex(-0.1, 0.6)
    glVertex(-0.2, 0.4)
    glVertex(-0.1, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(0.1, 0.6)
    glVertex(0.2, 0.4)
    glVertex(0.1, 0.4)

    glEnd()
    glColor3f(0, 0, 0.5)
    glBegin(GL_LINE_LOOP)
    glVertex(-0.1, 0.6)
    glVertex(-0.2, 0.4)
    glVertex(-0.1, 0.4)

    glEnd()







    glFlush()



glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(500,500)
glutCreateWindow(b"Lab2 Program")
glutDisplayFunc(draw)
glutMainLoop()