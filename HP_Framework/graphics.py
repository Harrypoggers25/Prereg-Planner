from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from PyQt5.QtCore import QRectF
from HP_Framework.objects import *

class HpGlWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.rects = []
        self.texts = []

    def initializeGL(self):
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def resizeGL(self, w, h):
        # print(f"W = {w}, H = {h}")
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, w, h, 0, -1, 1)  # Flip the y-axis to position the origin at the top-left corner
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        for rect in self.rects:
            self.renderRect(rect)

        painter = QtGui.QPainter(self)
        for text in self.texts:
            self.renderText(text, painter)

    def renderRect(self, rect : HpGlRect):
        glColor3f(rect.color.r / 255, rect.color.g / 255, rect.color.b/ 255)
        glBegin(GL_QUADS)
        glVertex2f(rect.x, rect.y)
        glVertex2f(rect.x + rect.w, rect.y)
        glVertex2f(rect.x + rect.w, rect.y + rect.h)
        glVertex2f(rect.x, rect.y + rect.h)
        glEnd()

    def renderText(self, text : HpGlText, painter : QtGui.QPainter):
        painter.beginNativePainting()
        painter.setPen(QtGui.QColor(text.color.r, text.color.g, text.color.b))
        painter.setFont(QtGui.QFont(text.font.family, text.font.size, text.font.weight, text.font.italic))
        painter.drawText(QRectF(text.x, text.y, text.width, text.height), Qt.AlignmentFlag.AlignLeft, text.val)
        painter.endNativePainting()

    def addRect(self, x, y, w, h, color):
        self.rects.append(HpGlRect(x, y, w, h, color))

    def addText(self, x, y, text, font, color, bcentered = False):
        gl_text = HpGlText(x, y, text, font, color, self)
        if bcentered:
            gl_text.setPosition(gl_text.x - gl_text.width / 2, gl_text.y - gl_text.height / 2)
        self.texts.append(gl_text)