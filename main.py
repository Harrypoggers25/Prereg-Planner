# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from HP_Framework.graphics import HpGlWidget
from Prereg_Engines.course_engine import CourseEngine
from Prereg_Engines.table_engine import TableEngine
from HP_Framework.objects import HpRgbColor, HpFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(738, 609)
        self.wgt_central = QtWidgets.QWidget(MainWindow)
        self.wgt_central.setObjectName("wgt_central")
        self.gridLayout = QtWidgets.QGridLayout(self.wgt_central)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.wgt_central)
        self.stackedWidget.setObjectName("stackedWidget")
        self.wgt_page1 = QtWidgets.QWidget()
        self.wgt_page1.setStyleSheet("#wgt_page1 {\n"
"    background-color: red;\n"
"}")
        self.wgt_page1.setObjectName("wgt_page1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wgt_page1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget.addWidget(self.wgt_page1)
        self.wgt_page2 = QtWidgets.QWidget()
        self.wgt_page2.setStyleSheet("#wgt_page2 {\n"
"    background-color: #e6e6e6;\n"
"}")
        self.wgt_page2.setObjectName("wgt_page2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.wgt_page2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frm_left = QtWidgets.QFrame(self.wgt_page2)
        self.frm_left.setMinimumSize(QtCore.QSize(0, 0))
        self.frm_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_left.setObjectName("frm_left")

        ####################### TEMPORARY WIDGETS #######################
        self.btn_left = QtWidgets.QPushButton(self.frm_left)
        self.btn_left.setGeometry(QtCore.QRect(10, 20, 93, 28))
        self.btn_left.setObjectName("btn_left")
        self.btn_right = QtWidgets.QPushButton(self.frm_left)
        self.btn_right.setGeometry(QtCore.QRect(100, 20, 93, 28))
        self.btn_right.setObjectName("btn_right")
        self.lbl_index = QtWidgets.QLabel(self.frm_left)
        self.lbl_index.setGeometry(QtCore.QRect(10, 50, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_index.setFont(font)
        self.lbl_index.setObjectName("lbl_index")
        #################################################################

        self.horizontalLayout_3.addWidget(self.frm_left)
        self.frm_right = QtWidgets.QFrame(self.wgt_page2)
        self.frm_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_right.setObjectName("frm_right")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frm_right)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.ogl_table = HpGlWidget(self.frm_right)
        self.ogl_table.setMinimumSize(QtCore.QSize(350, 532))
        self.ogl_table.setObjectName("ogl_table")

        self.gridLayout_2.addWidget(self.ogl_table, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frm_right)
        self.stackedWidget.addWidget(self.wgt_page2)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.wgt_central)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ----------------------TESTING---------------------- #
        self.course_engine = CourseEngine()
        self.course_engine.loadCourses(7, 0, 0)
        self.course_engine.selectCourse("ECIE 4101")
        self.course_engine.selectCourse("ECIE 4311")
        self.course_engine.selectCourse("ECIE 4312")
        self.course_engine.selectCourse("ECIE 4313")
        self.course_engine.selectCourse("ECIE 4351")
        self.course_engine.selectCourse("ECIE 4398")
        self.course_engine.selectCourse("EECE 3102")
        self.course_engine.selectCourse("MANU 3318")
        vtblcourses = self.course_engine.getVTableCourses()
        
        # W = 350, H = 532
        # print(f'Initial => W: {self.ogl_table.width()}, H: {self.ogl_table.height()}')
        b_selected_courses = [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True
        ]
        table_engine = TableEngine()
        table_engine.setVTblCourses(vtblcourses, b_selected_courses)
        
        combinations = table_engine.getCombinations(self.ogl_table.width(), self.ogl_table.height())
        self.ogl_table.setTableEngine(table_engine, self.btn_left, self.btn_right, self.lbl_index)
        self.ogl_table.setCombinations(combinations)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prereg Planner"))
        self.btn_left.setText(_translate("MainWindow", "<"))
        self.btn_right.setText(_translate("MainWindow", ">"))
        self.lbl_index.setText(_translate("MainWindow", "? / ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
