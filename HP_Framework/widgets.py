from OpenGL.GL import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import Qt, QRect

class HpGlWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.setMinimumSize(640, 480)
        self.rects = []
        self.texts = []

    def initializeGL(self):
        glDisable(GL_DEPTH_TEST)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, w, h, 0, -1, 1)  # Flip the y-axis to position the origin at the top-left corner
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        for rect in self.rects:
            self.renderRect(rect.x, rect.y, rect.w, rect.h, rect.color)

        painter = QtGui.QPainter(self)
        for text in self.texts:
            self.renderText(text.x, text.y, text.val, text.font, text.color, painter)

    def renderRect(self, x, y, w, h, color):
        glColor3f(color.r / 255, color.g / 255, color.b/ 255)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + w, y)
        glVertex2f(x + w, y + h)
        glVertex2f(x, y + h)
        glEnd()

    def renderText(self, x, y, text, font, color, painter : QtGui.QPainter):
        painter.beginNativePainting()
        painter.setPen(QtGui.QColor(color.r, color.g, color.b))
        painter.setFont(QtGui.QFont(font.family, font.size, font.weight, font.italic))
        font_metrics = painter.fontMetrics()
        rect = font_metrics.boundingRect(QRect(), Qt.AlignmentFlag.AlignLeft, text)
        painter.drawText(QRect(x, y, rect.width(), rect.height()), Qt.AlignmentFlag.AlignLeft, text)
        painter.endNativePainting()

    def addRect(self, x, y, w, h, color):
        self.rects.append(HpGlRect(x, y, w, h, color))

    def addText(self, x, y, text, font, color):
        self.texts.append(HPGlText(x, y, text, font, color))

class HpObject:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def setColor(self, color):
        del self.color
        self.color = color

class HpGlRect(HpObject):
    def __init__(self, x, y, w, h, color):
        HpObject.__init__(self, x, y, color)
        self.w = w
        self.h = h
    
    def setDimension(self, w, h):
        self.w = w
        self.h = h

    def setRect(self, x, y, w, h):
        self.setPosition(x, y)
        self.setDimension(w, h)

class HPGlText:
    def __init__(self, x, y, text, font, color):
        HpObject.__init__(self, x, y, color)
        self.val = text
        self.width = 0
        self.height = 0
        self.font = font
    
    def setText(self, text):
        self.val = text

    def setSize(self, size):
        self.font.size = size

    def setFont(self, font):
        self.font = font
   
class HpRgbColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

class HpFont:
    def __init__(self, family, size = 20, weight = 400, italic = False):
        self.family = family
        self.size = size
        self.weight = weight
        self.italic = italic
    