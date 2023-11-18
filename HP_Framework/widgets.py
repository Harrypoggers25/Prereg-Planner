from OpenGL.GL import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import Qt, QRect

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

class HpGlText:
    def __init__(self, x, y, text, font, color, painter : QtGui.QPainter):
        HpObject.__init__(self, x, y, color)
        self.font = font
        self.val = ''
        self.width = 0
        self.height = 0
        self.setText(text, painter)
    
    def setText(self, text, painter : QtGui.QPainter):
        painter.setFont(QtGui.QFont(self.font.family, self.font.size, self.font.weight, self.font.italic))
        font_metrics = painter.fontMetrics()
        rect = font_metrics.boundingRect(QRect(), Qt.AlignmentFlag.AlignLeft, text)
        self.width = rect.width()
        self.height = rect.height()
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
        painter.drawText(QRect(text.x, text.y, text.width, text.height), Qt.AlignmentFlag.AlignLeft, text.val)
        painter.endNativePainting()

    def addRect(self, x, y, w, h, color):
        self.rects.append(HpGlRect(x, y, w, h, color))

    def addText(self, x, y, text, font, color):
        self.texts.append(HpGlText(x, y, text, font, color, self))
    