from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluOrtho2D
import math

def circle(rx, ry, cx, cy):
    glBegin(GL_POLYGON)
    glVertex2f(cx, cy)
    for i in range(361):
        angle = i * 3.1416 / 180
        x = rx * math.cos(angle)
        y = ry * math.sin(angle)
        glVertex2f((x + cx), (y + cy))
    glEnd()

shift = 0  # a variable used to move the boat right and left
bx = 10

def init():
    glClearColor(0.0, 0.9, 0.9, 0.0)
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, 500, 0, 500)

def clouds():
    global bx
    glPushMatrix()
    glTranslatef(bx, 0, 0)
    
    # 1st cloud
    glColor3ub(255, 255, 255)
    circle(20, 30, 460, 460)
    circle(15, 20, 445, 460)
    circle(15, 20, 475, 460)

    # 2nd cloud
    circle(20, 30, 390, 420)
    circle(15, 20, 405, 420)
    circle(15, 20, 375, 420)

    glPopMatrix()
    bx += .05
    if bx > 0:
        bx = -500
    glutPostRedisplay()

def display():
    global shift
    glClear(GL_COLOR_BUFFER_BIT)

    # River Color
    glColor3ub(0, 191, 255)
    glBegin(GL_POLYGON)
    glVertex2d(0, 0)
    glVertex2d(500, 0)
    glVertex2d(500, 300)
    glVertex2d(0, 300)
    glEnd()

    # Boat design
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex2d(325 + shift, 220)
    glVertex2d(400 + shift, 220)
    glVertex2d(425 + shift, 250)
    glVertex2d(300 + shift, 250)
    glEnd()

    glColor3ub(205, 133, 63)
    glBegin(GL_POLYGON)
    glVertex2d(325 + shift, 250)
    glVertex2d(400 + shift, 250)
    glVertex2d(390 + shift, 280)
    glVertex2d(335 + shift, 280)
    glEnd()

    glColor3ub(160, 82, 45)
    glBegin(GL_POLYGON)
    glVertex2d(360 + shift, 280)
    glVertex2d(370 + shift, 280)
    glVertex2d(370 + shift, 310)
    glVertex2d(360 + shift, 310)
    glEnd()

    glColor3ub(34, 139, 34)
    glBegin(GL_POLYGON)
    glVertex2d(335 + shift, 290)
    glVertex2d(390 + shift, 290)
    glVertex2d(390 + shift, 375)
    glVertex2d(335 + shift, 375)
    glEnd()

    glColor3ub(255, 0, 0)
    circle(15, 20, 362 + shift, 330)

    # sun design
    glColor3ub(255, 215, 0)
    circle(25, 30, 175, 450)

    clouds()

    glFlush()
    glutSwapBuffers()

def key(key, x, y):
    global shift
    if key == GLUT_KEY_LEFT:
        shift -= 5
        glutPostRedisplay()
    elif key == GLUT_KEY_RIGHT:
        shift += 5
        glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("A Moving Boat")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(key)
    glutMainLoop()

main()