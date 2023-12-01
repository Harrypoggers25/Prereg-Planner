import sys
from PyQt5 import QtWidgets, QtCore, QtGui

class HpListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        QtWidgets.QListWidget.__init__(self, parent)
    
    def addItem(self, str1, str2, func=None):
        item = QtWidgets.QListWidgetItem()
        wgt = QtWidgets.QWidget()
        wgt.setStyleSheet("border: 1px solid black")
        lbl1 = QtWidgets.QLabel(str1)
        lbl1.setFixedSize(100, 50)
        lbl1.setStyleSheet("border: 1px solid black;")
        lbl2 = QtWidgets.QLabel(str2)
        lbl2.setStyleSheet("border: 1px solid black;")
        lbl2.setScaledContents(True)
        btn = QtWidgets.QPushButton("+")
        btn.setFixedSize(50, 50)
        btn.setStyleSheet("background-color: green; color: white; font-size: 20px; font-weight: bold;")
        if func:
            btn.clicked.connect(func)

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(lbl1)
        layout.addWidget(lbl2)
        layout.addWidget(btn)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        wgt.setLayout(layout)
        item.setSizeHint(wgt.sizeHint())
        super().addItem(item)
        self.setItemWidget(item, wgt)

class HpTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        QtWidgets.QTableWidget.__init__(self, parent)
        self.setColumnCount(3)
        self.horizontalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.verticalHeader().hide()
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.setStyleSheet("QTableWidget { border: 1px solid black; }")

    def setTableType(self, type):
        if type == "select":
            self.setStyleSheet("QTableWidget, QPushButton, QLabel { border: 1px solid black; }"
                               "QPushButton { background-color: #cdea8c; }"
                               "QPushButton::pressed { background-color: #9aad49; }")
        elif type == "deselect":
            self.setStyleSheet("QTableWidget, QPushButton, QLabel { border: 1px solid black; }"
                               "QPushButton { background-color: #fecbcc; }"
                               "QPushButton::pressed { background-color: #b87b7d; }")

    def addItem(self, str1, str2, str3, func=None):
        row_position = self.rowCount()
        self.insertRow(row_position)

        lbl1 = QtWidgets.QLabel(str1)

        lbl2 = QtWidgets.QLabel(str2)
        
        btn = QtWidgets.QPushButton(str3)
        btn.setFixedSize(50, 50)
        if func:
            btn.clicked.connect(func)

        self.setCellWidget(row_position, 0, lbl1)
        self.setCellWidget(row_position, 1, lbl2)
        self.setCellWidget(row_position, 2, btn)

    

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("List Item with button")

        self.centralwidgetHorizontalLayout = QtWidgets.QHBoxLayout(self)

        self.Frame = QtWidgets.QGroupBox()  
        self.FrameHorizontalLayout = QtWidgets.QHBoxLayout(self.Frame)

        self.ListWidget = HpTableWidget(self.Frame)

        self.FrameHorizontalLayout.addWidget(self.ListWidget)
        self.centralwidgetHorizontalLayout.addWidget(self.Frame)

        self.ListWidget.setTableType("select")
        self.ListWidget.addItem("no 1", "huhuasdasdasdasdasdasdasdasdasdassdasdasdasd", "+", lambda: self.hehe())
        self.ListWidget.addItem("hehe", "huhu", "+")
        self.ListWidget.addItem("hehe", "huhu", "+")
        self.ListWidget.addItem("hehe", "huhu", "+")
        self.ListWidget.addItem("hehe", "huhu", "+")
        self.ListWidget.addItem("hehe", "huhu", "+")

    def hehe(self):
        self.ListWidget.clear()
        self.ListWidget.setRowCount(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())