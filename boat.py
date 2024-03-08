from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import gluPerspective, gluLookAt

rotation_angle = 1
bx = 6
moon_position = [-5.0, 3.0, -5.0]  # Ganti nilai sesuai keinginan

def init():
    # glClearColor(0.0, 0.9, 0.9, 0.0)
    glClearColor(0.0, 0.0, 0.2, 1.0)  # Warna latar belakang biru tua

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Warna pencahayaan abu-abu kebiruan

    glEnable(GL_LIGHT0)

    light_position = [1, 1, 1, 0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 1, 100)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(5, 5, 10, 0, 0, 0, 0, 1, 0)

def draw_boat():
    global bx
    glTranslatef(0, 0, bx)

    # Body of the boat
    glColor3ub(50, 50, 50)
    glBegin(GL_POLYGON)
    glVertex3d(-1, 0, 1)
    glVertex3d(1, 0, 1)
    glVertex3d(0.7, 0, -1)
    glVertex3d(-0.7, 0, -1)
    glEnd()

    # Front of the boat
    glColor3ub(50, 50, 50)
    glBegin(GL_TRIANGLES)
    glVertex3d(0, 0, 1)
    glVertex3d(0.7, 0, -1)
    glVertex3d(-0.7, 0, -1)
    glEnd()

    # Sail
    glColor3ub(255, 0, 0)
    glBegin(GL_TRIANGLES)
    glVertex3d(0, 2, 0)
    glVertex3d(0, 0, 1)
    glVertex3d(0, 0, -1)
    glEnd()

    # Right side
    glColor3ub(139, 69, 19)
    glBegin(GL_QUADS)
    glVertex3d(0.7, 0, 1)
    glVertex3d(0.7, 0, -1)
    glVertex3d(0.5, 0.5, -1)
    glVertex3d(0.5, 0.5, 1)
    glEnd()

    # Left side
    glColor3ub(139, 69, 19)
    glBegin(GL_QUADS)
    glVertex3d(-0.7, 0, 1)
    glVertex3d(-0.7, 0, -1)
    glVertex3d(-0.5, 0.5, -1)
    glVertex3d(-0.5, 0.5, 1)
    glEnd()

    # Back side
    glColor3ub(139, 69, 19)
    glBegin(GL_TRIANGLES)
    glVertex3d(-0.7, 0, -1)
    glVertex3d(0, 0.5, -1)
    glVertex3d(0.7, 0, -1)
    glEnd()

    # Stern
    glColor3ub(139, 69, 19)
    glBegin(GL_QUADS)
    glVertex3d(0.3, 0, -1)
    glVertex3d(0.3, 0.5, -1)
    glVertex3d(-0.3, 0.5, -1)
    glVertex3d(-0.3, 0, -1)
    glEnd()

    # Bridge
    glColor3ub(139, 69, 19)
    glBegin(GL_QUADS)
    glVertex3d(0.1, 0., 0.8)
    glVertex3d(0.1, 0.5, 0.8)
    glVertex3d(-0.1, 0.5, 0.8)
    glVertex3d(-0.1, 0.3, 0.8)
    glEnd()

def init_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)

    # Menetapkan posisi lampu
    light_position = [0, 5, 0, 1]
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

    # Menetapkan warna cahaya
    light_ambient = [0.3, 0.3, 0.3, 1.0]
    light_diffuse = [1.0, 1.0, 1.0, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

def draw_moon():
    # glTranslatef(moon_position[0], moon_position[1], moon_position[2])
    glColor3ub(255, 255, 255)
    glutSolidSphere(1.0, 50, 50)

def draw_mountains1():
    glColor3ub(139, 115, 85)  # Warna gunung, bisa disesuaikan

    # Menentukan norma permukaan gunung untuk shading
    normal = [0, 0, 1]
    glNormal3fv(normal)
    glBegin(GL_TRIANGLES)
    glVertex3d(-7, 0, -5)
    glVertex3d(0, 3, -5)
    glVertex3d(3, 0, -5)
    glEnd()

def draw_mountains2():
    glColor3ub(139, 115, 85)  # Warna gunung, bisa disesuaikan
    glBegin(GL_TRIANGLES)
    glVertex3d(-3, 0, -5)
    glVertex3d(0, 3, -5)
    glVertex3d(3, 0, -5)
    glEnd()



def display():
    global rotation_angle, bx
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    init_lighting()

    glPushMatrix()
    # glutPostRedisplay()
    glRotatef(rotation_angle, 1, 0, 0)
    glPushMatrix()
    glTranslatef(moon_position[0], moon_position[1], moon_position[2])
    draw_moon()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-5, 0, 6)
    draw_mountains1()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(5, 0, 6)
    draw_mountains2()
    glPopMatrix()

    draw_boat()

    # Shadow
    glColor4f(0.1, 0.1, 0.1, 0.5)
    glBegin(GL_QUADS)
    glVertex3d(-1, 0, 1)
    glVertex3d(1, 0, 1)
    glVertex3d(0.7, 0, -1)
    glVertex3d(-0.7, 0, -1)
    glEnd()
    glEnable(GL_LIGHTING)

    glPopMatrix()
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("A Rotating Boat")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(update)
    glutMainLoop()

def update():
    global rotation_angle, bx
    # rotation_angle += 0.1
    # if rotation_angle > 360.0:
    #     rotation_angle -= 360.0

    #mengatur translasi/ perindahan. menggunakan sumbu z
    bx -= 0.002
    if bx < -40.0:  # Sesuaikan nilai batas ujung
        bx = 6.0

    glutPostRedisplay()

main()