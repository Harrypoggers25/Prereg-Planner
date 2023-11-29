from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5 import QtWidgets
from OpenGL.GL import *
from PyQt5.QtCore import QRectF
from HP_Framework.objects import *
from Prereg_Engines.table_engine import TableEngine

class HpGlWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.rects = []
        self.texts = []
        self.tbl_engine = None
        self.lbl_index = None

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

    ################################## LOW LEVEL IMPLEMETATION ##################################
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

    def addText(self, x, y, text, font, color, bcenterx = False, bcentery = False):
        gl_text = HpGlText(x, y, text, font, color, self)
        if bcenterx:
            x = gl_text.x - gl_text.width / 2
        if bcentery:
            y = gl_text.y - gl_text.height / 2
        if bcenterx or bcentery:
            gl_text.setPosition(x, y)
        # if bcenterx and not bcentery:
        #     print(f'X: {gl_text.x}, Y: {gl_text.y}, W: {gl_text.width}, H: {gl_text.height}')
        self.texts.append(gl_text)
    
    ################################## HIGH LEVEL IMPLEMETATION ##################################
    def setTableEngine(self, table_engine : TableEngine, btn_left : QtWidgets.QPushButton, btn_right : QtWidgets.QPushButton, lbl_index : QtWidgets.QLabel):
        self.tbl_engine = table_engine
        self.lbl_index = lbl_index
        btn_left.clicked.connect(lambda: self.btnLeftPressed())
        btn_right.clicked.connect(lambda: self.btnRightPressed())

        table_engine.setIndex(0)
    
    def setCombinations(self, combinations):
        self.rects.clear()
        self.texts.clear()
        if self.tbl_engine:
            for table in combinations:
                for rects in table.vrects:
                    for rect in rects:
                        self.addRect(rect.x, rect.y, rect.w, rect.h, table.color)
                        # print(f'{table.code} => X: {rect.x}, Y: {rect.y}, W: {rect.w}, H: {rect.h}')
            font = HpFont("Roboto", 10, 600)
            for text in self.tbl_engine.texts[0]:
                self.addText(text.x, text.y, text.val, font, HpRgbColor(255, 255, 255), True)
            font = HpFont("Roboto", 6, 600)
            for text in self.tbl_engine.texts[1]:
                self.addText(text.x, text.y, text.val, font, HpRgbColor(255, 255, 255), True, True)

            self.lbl_index.setText(f"{self.tbl_engine.index + 1} / {self.tbl_engine.getVCombinationsSize()}")

    def btnLeftPressed(self):
        if self.tbl_engine:
            if self.tbl_engine.index - 1 >= 0:
                self.tbl_engine.setIndex(self.index - 1)
            else:
                print('reached minimum')    # TEMPORARY
    
    def btnRightPressed(self):
        if self.tbl_engine:
            if self.tbl_engine.index + 1 < self.tbl_engine.getVCombinationsSize():
                self.tbl_engine.setIndex(self.index + 1)
            else:
                print('reached maximum')    # TEMPORARY
