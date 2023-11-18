from PyQt5 import QtWidgets, QtOpenGL
from HP_Framework.widgets import HpGlWidget, HpRgbColor, HpFont

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.widget = HpGlWidget()
        self.widget.addRect(0, 0, 100, 100, HpRgbColor(255, 255, 0))
        self.widget.addRect(100, 100, 100, 100, HpRgbColor(255, 0, 0))
        self.widget.addRect(200, 200, 100, 100, HpRgbColor(0, 0, 255))
        self.widget.addRect(300, 300, 100, 100, HpRgbColor(0, 255, 0))
        font = HpFont("Arial", 10, 600)
        self.widget.addText(300, 300, "EECE 1234", font, HpRgbColor(255, 255, 255))
        self.widget.addText(300, 315, "EECE 1234", font, HpRgbColor(255, 255, 255))
        mainLayout = QtWidgets.QHBoxLayout()
        mainLayout.addWidget(self.widget)
        self.setLayout(mainLayout)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainWindow(Form)
    ui.show()
    app.exec_()
