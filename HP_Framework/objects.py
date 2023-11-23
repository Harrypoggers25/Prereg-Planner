from PyQt5.QtCore import Qt, QRect
from PyQt5 import QtGui

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