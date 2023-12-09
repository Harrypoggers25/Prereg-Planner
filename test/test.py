# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

class HpRgbColor:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
HpRgbColor.BLACK = HpRgbColor(0, 0, 0)
HpRgbColor.WHITE = HpRgbColor(255, 255, 255)

from PyQt5 import QtCore, QtGui, QtWidgets

class HpListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super(HpListWidget, self).__init__(parent)
        self.cbs = []   #checkboxes
        self.vcolors_default = []   # HpRgbColor
        self.vcolors_current = []   # HpRgbColor
        self.swgts = [] # stacked widgets
        
        self.setStyleSheet('QListWidget::item { border: 2px solid black }')
        self.setSpacing(4)

    def setDefaultVColors(self, vcolors):
        self.vcolors_default = vcolors

    def addItem(self, title : str, code : str, sects : list, color_index: int):
        self.vcolors_current.append(self.vcolors_default[color_index])

        # setup ui
        swgt = QtWidgets.QStackedWidget()

        wgt1 = QtWidgets.QWidget()
        wgt1.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        hlayout1 = QtWidgets.QHBoxLayout(wgt1)
        self.cbs.append(HpCheckBox('Assets/Images/cb.png', 'Assets/Images/cb_checked.png', wgt1))
        self.cbs[-1].setFixedSize(40, 40)
        frm1 = QtWidgets.QFrame(wgt1)
        vlayout1 = QtWidgets.QVBoxLayout(frm1)
        lbl1 = QtWidgets.QLabel(title)
        font = QtGui.QFont('roboto', 10, 600, False)
        lbl1.setFont(font)
        font.setWeight(400)
        lbl2 = QtWidgets.QLabel(code)
        lbl2.setFont(font)
        lbl3 = QtWidgets.QLabel(f'Sections: {sects}')
        lbl3.setFont(font)
        vlayout1.addWidget(lbl1)
        vlayout1.addWidget(lbl2)
        vlayout1.addWidget(lbl3)
        frm1.setLayout(vlayout1)
        btn = QtWidgets.QPushButton(wgt1)
        btn.setFixedSize(40, 40)
        btn.setStyleSheet(f'background-color: rgb({self.vcolors_default[color_index][0].r},{self.vcolors_default[color_index][0].g},{self.vcolors_default[color_index][0].b});')
        hlayout1.addWidget(self.cbs[-1])
        hlayout1.addWidget(frm1)
        hlayout1.addWidget(btn)
        wgt1.setLayout(hlayout1)
        
        wgt2 = QtWidgets.QWidget()
        hlayout2 = QtWidgets.QHBoxLayout(wgt2)
        scbtns = []
        def rtnlambda1(b, c, i):
            return lambda: self.scbtn_clicked(b, c, i)
        for colors in self.vcolors_default:
            scbtns.append(QtWidgets.QPushButton(wgt2))
            scbtns[-1].setStyleSheet(f'background-color: rgb({colors[0].r},{colors[0].g},{colors[0].b});')
            scbtns[-1].setFixedSize(40, 40)
            n_colors = self.vcolors_default[len(scbtns) - 1]
            scbtns[-1].clicked.connect(rtnlambda1(btn, n_colors, len(self.swgts)))
        hspacer = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        frm2 = QtWidgets.QFrame(wgt2)
        vlayout2 = QtWidgets.QVBoxLayout(frm2)
        btn_close = QtWidgets.QPushButton(frm2)
        btn_close.setStyleSheet('color: red;')
        font.setWeight(600)
        btn_close.setFont(font)
        btn_close.setText('x')
        btn_close.setFixedSize(30, 30)
        vspacer = QtWidgets.QSpacerItem(0, 0,  QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        vlayout2.addWidget(btn_close)
        vlayout2.addItem(vspacer)
        frm2.setLayout(vlayout2)
        for scbtn in scbtns:
            hlayout2.addWidget(scbtn)
        hlayout2.addItem(hspacer)
        hlayout2.addWidget(frm2)
        wgt2.setLayout(hlayout2)

        swgt.addWidget(wgt1)
        swgt.addWidget(wgt2)

        self.swgts.append(swgt)

        btn_close.clicked.connect(lambda: swgt.setCurrentIndex(0))
        def rtnlambda2(i):
            return lambda: self.btn_clicked(i)
        btn.clicked.connect(rtnlambda2(len(self.swgts) - 1))

        item = QtWidgets.QListWidgetItem(self)
        item.setSizeHint(swgt.sizeHint())
        super().addItem(item)
        self.setItemWidget(item, swgt)

    def btn_clicked(self, index):
        for i in range(len(self.swgts)):
            if i == index:
                self.swgts[i].setCurrentIndex(1)
            else:
                self.swgts[i].setCurrentIndex(0)
    
    def scbtn_clicked(self, btn, colors, i):
        self.vcolors_current[i] = colors
        btn.setStyleSheet(f'background-color: rgb({colors[0].r},{colors[0].g},{colors[0].b});')
        self.swgts[i].setCurrentIndex(0)
        
    def getCheckedItems(self):
        return [cb.isChecked() for cb in self.cbs]
    
    def getCurrentColors(self):
        return self.vcolors_current
    
    def clear(self):
        self.swgts.clear()
        super().clear()
    
class HpCheckBox(QtWidgets.QAbstractButton):
    def __init__(self, img, img_checked, parent=None):
        super(HpCheckBox, self).__init__(parent)
        self.checked = False
        self.pixmaps = [QtGui.QPixmap(img), QtGui.QPixmap(img_checked)]
        self.current_pixmap = self.pixmaps[0]

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(self.current_pixmap.rect(), self.current_pixmap)

    def sizeHint(self):
        return self.current_pixmap.size()

    def mousePressEvent(self, e):
        self.checked = not self.checked
        if self.checked:
            self.current_pixmap = self.pixmaps[1]
        else:
            self.current_pixmap = self.pixmaps[0]
        return super().mousePressEvent(e)

    def isChecked(self):
        return self.checked

class HpImageButton(QtWidgets.QAbstractButton):
    def __init__(self, img, img_hovered, img_pressed, parent=None):
        super(HpImageButton, self).__init__(parent)
        self.pixmaps = [QtGui.QPixmap(img), QtGui.QPixmap(img_hovered), QtGui.QPixmap(img_pressed)]
        self.current_pixmap = self.pixmaps[0]
        self.previous_pixmap = None
    
    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(event.rect(), self.current_pixmap)

    def sizeHint(self):
        return self.current_pixmap.size()
    
    def mouseReleaseEvent(self, e):
        self.current_pixmap = self.pixmaps[1]
        return super().mouseReleaseEvent(e)

    def enterEvent(self, a0):
        self.current_pixmap = self.pixmaps[1]
        return super().enterEvent(a0)

    def leaveEvent(self, a0):
        self.current_pixmap = self.pixmaps[0]
        return super().leaveEvent(a0)

    def mousePressEvent(self, e):
        self.current_pixmap = self.pixmaps[2]
        return super().mousePressEvent(e)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(854, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lwgt = HpListWidget(self.centralwidget)
        self.lwgt.setObjectName("lwgt")
        self.gridLayout.addWidget(self.lwgt, 2, 0, 1, 1)
        self.btn_check = QtWidgets.QPushButton(self.centralwidget)
        self.btn_check.setObjectName("btn_check")
        self.gridLayout.addWidget(self.btn_check, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        VCOLORS = [
            [HpRgbColor(238, 36, 36), HpRgbColor.WHITE],
            [HpRgbColor(239, 81, 34), HpRgbColor.WHITE],
            [HpRgbColor(22, 87, 143), HpRgbColor.WHITE],
            [HpRgbColor(20, 175, 74), HpRgbColor.WHITE],
            [HpRgbColor(173, 20, 175), HpRgbColor.WHITE],
            [HpRgbColor(0, 94, 33),   HpRgbColor.WHITE],
            [HpRgbColor(80, 100, 0),  HpRgbColor.WHITE],
            [HpRgbColor(2, 183, 164), HpRgbColor.WHITE],
            [HpRgbColor(175, 92, 37), HpRgbColor.WHITE],
            [HpRgbColor(239, 88, 61), HpRgbColor.WHITE],
            [HpRgbColor(50, 80, 140), HpRgbColor.WHITE],
            [HpRgbColor(241, 85, 98), HpRgbColor.WHITE]
        ]
        self.lwgt.setDefaultVColors(VCOLORS)

        self.lwgt.addItem("COMPUTER INFORMATION ENGINEERING", "ECIE 4101", [1, 2, 3], 0)
        self.lwgt.addItem("SOFTWARE ENGINEERING DESIGN", "ECIE 4311", [1, 2], 1)
        self.lwgt.addItem("MULTIMEDIA INFORMATION SYSTEM", "ECIE 4312", [1, 2], 2)
        self.lwgt.addItem("COMPUTER COMMUNICATION AND NETWORKING", "ECIE 4313", [1, 2, 3], 3)
        self.lwgt.addItem("OBJECT ORIENTED PROGRAMMING", "ECIE 4351", [2, 3], 4)
        self.lwgt.addItem("FINAL YEAR PROJECT I", "ECIE 4398", [1, 3], 5)

        # self.btn_check.clicked.connect(lambda: print(self.lwgt.getCheckedItems()))
        self.btn_check.clicked.connect(lambda: self.lwgt.clear())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_check.setText(_translate("MainWindow", "Check"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
