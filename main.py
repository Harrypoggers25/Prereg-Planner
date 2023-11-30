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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(624, 588)
        self.wgt_central = QtWidgets.QWidget(MainWindow)
        self.wgt_central.setObjectName("wgt_central")
        self.gridLayout = QtWidgets.QGridLayout(self.wgt_central)
        self.gridLayout.setObjectName("gridLayout")
        self.swgt_1 = QtWidgets.QStackedWidget(self.wgt_central)
        self.swgt_1.setObjectName("swgt_1")
        self.wgt_page1 = QtWidgets.QWidget()
        self.wgt_page1.setStyleSheet("#wgt_page1 {\n"
"    background-color: red;\n"
"}")
        self.wgt_page1.setObjectName("wgt_page1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wgt_page1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.swgt_1.addWidget(self.wgt_page1)
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frm_left)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btn_right = QtWidgets.QPushButton(self.frm_left)
        self.btn_right.setObjectName("btn_right")
        self.gridLayout_4.addWidget(self.btn_right, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 2)
        self.btn_left = QtWidgets.QPushButton(self.frm_left)
        self.btn_left.setObjectName("btn_left")
        self.gridLayout_4.addWidget(self.btn_left, 0, 0, 1, 1)
        self.lbl_index = QtWidgets.QLabel(self.frm_left)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_index.setFont(font)
        self.lbl_index.setStyleSheet("#lbl_index{\n"
"    text-align: center;\n"
"}")
        self.lbl_index.setObjectName("lbl_index")
        self.gridLayout_4.addWidget(self.lbl_index, 1, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.frm_left)
        self.frm_right = QtWidgets.QFrame(self.wgt_page2)
        self.frm_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_right.setObjectName("frm_right")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frm_right)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.swgt_2 = QtWidgets.QStackedWidget(self.frm_right)
        self.swgt_2.setObjectName("swgt_2")
        self.wgt_page2_1 = QtWidgets.QWidget()
        self.wgt_page2_1.setObjectName("wgt_page2_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.wgt_page2_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.ogl_table = HpGlWidget(self.wgt_page2_1)
        self.ogl_table.setMinimumSize(QtCore.QSize(350, 532))
        self.ogl_table.setObjectName("ogl_table")
        self.gridLayout_3.addWidget(self.ogl_table, 0, 0, 1, 1)
        self.swgt_2.addWidget(self.wgt_page2_1)
        self.wgt_page2_2 = QtWidgets.QWidget()
        self.wgt_page2_2.setObjectName("wgt_page2_2")
        self.swgt_2.addWidget(self.wgt_page2_2)
        self.gridLayout_2.addWidget(self.swgt_2, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frm_right)
        self.swgt_1.addWidget(self.wgt_page2)
        self.gridLayout.addWidget(self.swgt_1, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.wgt_central)

        self.retranslateUi(MainWindow)
        self.swgt_1.setCurrentIndex(1)
        self.swgt_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prereg Planner"))
        self.btn_right.setText(_translate("MainWindow", ">"))
        self.btn_left.setText(_translate("MainWindow", "<"))
        self.lbl_index.setText(_translate("MainWindow", "? / ?"))

    def run(self):
        #************************IMPLEMENTATION************************#
        ############################ PAGE 1 ############################
        
        self.course_engine = CourseEngine()
        self.course_engine.loadCourses(7, 0, 0) # Loads Engin Kulliyah's Subjects
        # ----------------------TEST 1---------------------- #  4th year subjects
        # self.course_engine.selectCourse("ECIE 4101")
        # self.course_engine.selectCourse("ECIE 4311")
        # self.course_engine.selectCourse("ECIE 4312")
        # self.course_engine.selectCourse("ECIE 4313")
        # self.course_engine.selectCourse("ECIE 4351")
        # self.course_engine.selectCourse("ECIE 4398")
        # self.course_engine.selectCourse("EECE 3102")
        # self.course_engine.selectCourse("MANU 3318")
        # ----------------------TEST 2---------------------- #  1st year subjects
        self.course_engine.selectCourse('EECE 1101')
        self.course_engine.selectCourse('EECE 1312')
        self.course_engine.selectCourse('EECE 1313')
        self.course_engine.selectCourse('MATH 1320')
        self.course_engine.selectCourse('MECH 1302')
        self.course_engine.deselectCourse('EECE 1101')
        
        ############################ PAGE 2 ############################
        vtblcourses = self.course_engine.getVTableCourses() # vector list of course tables
        n_chs = self.course_engine.getCHs() # list of credit hours
        b_selected_courses = [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ]
        table_engine = TableEngine()
        table_engine.setVTblCourses(vtblcourses, n_chs, b_selected_courses)
        
        combinations = table_engine.getCombinations(self.ogl_table.width(), self.ogl_table.height())
        self.ogl_table.setTableEngine(table_engine, self.btn_left, self.btn_right, self.lbl_index)
        self.ogl_table.setCombinations(combinations)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.run()
    MainWindow.show()
    sys.exit(app.exec_())
