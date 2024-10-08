# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from HP_Framework.graphics import HpGlWidget, HpTableWidget
from Prereg_Engines.course_engine import CourseEngine
from Prereg_Engines.table_engine import TableEngine

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 695)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.wgt_central = QtWidgets.QWidget(MainWindow)
        self.wgt_central.setObjectName("wgt_central")
        self.gridLayout = QtWidgets.QGridLayout(self.wgt_central)
        self.gridLayout.setObjectName("gridLayout")
        self.swgt_1 = QtWidgets.QStackedWidget(self.wgt_central)
        self.swgt_1.setObjectName("swgt_1")
        self.wgt_page1 = QtWidgets.QWidget()
        self.wgt_page1.setStyleSheet("")
        self.wgt_page1.setObjectName("wgt_page1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.wgt_page1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_top = QtWidgets.QFrame(self.wgt_page1)
        self.frm_top.setStyleSheet("")
        self.frm_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top.setObjectName("frm_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_top)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frm_top_left = QtWidgets.QFrame(self.frm_top)
        self.frm_top_left.setStyleSheet("")
        self.frm_top_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_left.setObjectName("frm_top_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_top_left)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frm_top_left_top = QtWidgets.QFrame(self.frm_top_left)
        self.frm_top_left_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_left_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_left_top.setObjectName("frm_top_left_top")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frm_top_left_top)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frm_kulliyah = QtWidgets.QFrame(self.frm_top_left_top)
        self.frm_kulliyah.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_kulliyah.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_kulliyah.setObjectName("frm_kulliyah")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frm_kulliyah)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbl_kulliyah = QtWidgets.QLabel(self.frm_kulliyah)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_kulliyah.setFont(font)
        self.lbl_kulliyah.setObjectName("lbl_kulliyah")
        self.horizontalLayout_4.addWidget(self.lbl_kulliyah)
        self.cb_kulliyah = QtWidgets.QComboBox(self.frm_kulliyah)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.cb_kulliyah.setFont(font)
        self.cb_kulliyah.setObjectName("cb_kulliyah")
        self.horizontalLayout_4.addWidget(self.cb_kulliyah)
        self.horizontalLayout_2.addWidget(self.frm_kulliyah)
        self.verticalLayout_2.addWidget(self.frm_top_left_top)
        self.frm_top_left_bottom = QtWidgets.QFrame(self.frm_top_left)
        self.frm_top_left_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_left_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_left_bottom.setObjectName("frm_top_left_bottom")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frm_top_left_bottom)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frm_session = QtWidgets.QFrame(self.frm_top_left_bottom)
        self.frm_session.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_session.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_session.setObjectName("frm_session")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frm_session)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lbl_session = QtWidgets.QLabel(self.frm_session)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_session.setFont(font)
        self.lbl_session.setObjectName("lbl_session")
        self.horizontalLayout_7.addWidget(self.lbl_session)
        self.cb_session = QtWidgets.QComboBox(self.frm_session)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.cb_session.setFont(font)
        self.cb_session.setObjectName("cb_session")
        self.horizontalLayout_7.addWidget(self.cb_session)
        self.horizontalLayout_6.addWidget(self.frm_session)
        self.frm_type = QtWidgets.QFrame(self.frm_top_left_bottom)
        self.frm_type.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_type.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_type.setObjectName("frm_type")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frm_type)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.lbl_type = QtWidgets.QLabel(self.frm_type)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_type.setFont(font)
        self.lbl_type.setObjectName("lbl_type")
        self.horizontalLayout_5.addWidget(self.lbl_type)
        self.cb_type = QtWidgets.QComboBox(self.frm_type)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.cb_type.setFont(font)
        self.cb_type.setObjectName("cb_type")
        self.horizontalLayout_5.addWidget(self.cb_type)
        self.horizontalLayout_6.addWidget(self.frm_type)
        self.verticalLayout_2.addWidget(self.frm_top_left_bottom)
        self.horizontalLayout.addWidget(self.frm_top_left)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.frm_top_right = QtWidgets.QFrame(self.frm_top)
        self.frm_top_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_top_right.setObjectName("frm_top_right")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frm_top_right)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_load_courses = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_load_courses.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_load_courses.setFont(font)
        self.btn_load_courses.setIconSize(QtCore.QSize(16, 16))
        self.btn_load_courses.setObjectName("btn_load_courses")
        self.verticalLayout_3.addWidget(self.btn_load_courses)
        self.lbl_or = QtWidgets.QLabel(self.frm_top_right)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.lbl_or.setFont(font)
        self.lbl_or.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_or.setObjectName("lbl_or")
        self.verticalLayout_3.addWidget(self.lbl_or)
        self.btn_open_file = QtWidgets.QPushButton(self.frm_top_right)
        self.btn_open_file.setMinimumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_open_file.setFont(font)
        self.btn_open_file.setStyleSheet("#btn_open_file{\n"
"    background-color: #f8c600;\n"
"    border-radius: 5%;\n"
"}\n"
"#btn_open_file::pressed{\n"
"    background-color: #dcb000;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/Icons/arrow-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_open_file.setIcon(icon)
        self.btn_open_file.setIconSize(QtCore.QSize(25, 25))
        self.btn_open_file.setDefault(False)
        self.btn_open_file.setFlat(False)
        self.btn_open_file.setObjectName("btn_open_file")
        self.verticalLayout_3.addWidget(self.btn_open_file)
        self.horizontalLayout.addWidget(self.frm_top_right)
        self.verticalLayout.addWidget(self.frm_top)
        self.frm_bottom = QtWidgets.QFrame(self.wgt_page1)
        self.frm_bottom.setMinimumSize(QtCore.QSize(764, 505))
        self.frm_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_bottom.setObjectName("frm_bottom")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frm_bottom)
        self.gridLayout_5.setHorizontalSpacing(15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frm_loaded_courses_header = QtWidgets.QFrame(self.frm_bottom)
        self.frm_loaded_courses_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_loaded_courses_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_loaded_courses_header.setObjectName("frm_loaded_courses_header")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frm_loaded_courses_header)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lbl_loaded_courses = QtWidgets.QLabel(self.frm_loaded_courses_header)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_loaded_courses.setFont(font)
        self.lbl_loaded_courses.setObjectName("lbl_loaded_courses")
        self.horizontalLayout_8.addWidget(self.lbl_loaded_courses)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.frm_search = QtWidgets.QFrame(self.frm_loaded_courses_header)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.frm_search.setFont(font)
        self.frm_search.setAutoFillBackground(False)
        self.frm_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frm_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frm_search.setObjectName("frm_search")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frm_search)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_search = QtWidgets.QLabel(self.frm_search)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lbl_search.setFont(font)
        self.lbl_search.setObjectName("lbl_search")
        self.horizontalLayout_9.addWidget(self.lbl_search)
        self.tb_search = QtWidgets.QLineEdit(self.frm_search)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.tb_search.setFont(font)
        self.tb_search.setStyleSheet("border-radius: 5%;")
        self.tb_search.setFrame(False)
        self.tb_search.setObjectName("tb_search")
        self.horizontalLayout_9.addWidget(self.tb_search)
        self.horizontalLayout_8.addWidget(self.frm_search)
        self.gridLayout_5.addWidget(self.frm_loaded_courses_header, 0, 0, 1, 1)
        self.twgt_loaded_courses = HpTableWidget(self.frm_bottom)
        self.twgt_loaded_courses.setMinimumSize(QtCore.QSize(323, 0))
        self.twgt_loaded_courses.setObjectName("twgt_loaded_courses")
        self.twgt_loaded_courses.setColumnCount(0)
        self.twgt_loaded_courses.setRowCount(0)
        self.gridLayout_5.addWidget(self.twgt_loaded_courses, 2, 0, 1, 1)
        self.twgt_selected_courses = HpTableWidget(self.frm_bottom)
        self.twgt_selected_courses.setMinimumSize(QtCore.QSize(323, 0))
        self.twgt_selected_courses.setObjectName("twgt_selected_courses")
        self.twgt_selected_courses.setColumnCount(0)
        self.twgt_selected_courses.setRowCount(0)
        self.gridLayout_5.addWidget(self.twgt_selected_courses, 2, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.frm_bottom)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_selected_courses = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_selected_courses.setFont(font)
        self.lbl_selected_courses.setObjectName("lbl_selected_courses")
        self.horizontalLayout_10.addWidget(self.lbl_selected_courses)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.btn_generate = QtWidgets.QPushButton(self.frame)
        self.btn_generate.setEnabled(True)
        self.btn_generate.setMinimumSize(QtCore.QSize(160, 40))
        self.btn_generate.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.btn_generate.setFont(font)
        self.btn_generate.setStyleSheet("#btn_generate{\n"
"    background-color: #00bb00;\n"
"    border-radius: 5%;\n"
"}\n"
"#btn_generate::pressed{\n"
"    background-color: green;\n"
"}\n"
"#btn_generate::disabled{\n"
"    background-color: #a5ffa5;\n"
"    color: #777777;\n"
"}")
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_10.addWidget(self.btn_generate)
        self.gridLayout_5.addWidget(self.frame, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.frm_bottom)
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
        self.btn_save = QtWidgets.QPushButton(self.frm_left)
        self.btn_save.setObjectName("btn_save")
        self.gridLayout_4.addWidget(self.btn_save, 1, 0, 1, 2)
        self.lbl_index = QtWidgets.QLabel(self.frm_left)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_index.setFont(font)
        self.lbl_index.setStyleSheet("#lbl_index{\n"
"    text-align: center;\n"
"}")
        self.lbl_index.setObjectName("lbl_index")
        self.gridLayout_4.addWidget(self.lbl_index, 6, 0, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 15, 0, 1, 2)
        self.btn_add = QtWidgets.QPushButton(self.frm_left)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout_4.addWidget(self.btn_add, 0, 0, 1, 2)
        self.btn_right = QtWidgets.QPushButton(self.frm_left)
        self.btn_right.setObjectName("btn_right")
        self.gridLayout_4.addWidget(self.btn_right, 4, 1, 1, 1)
        self.btn_left = QtWidgets.QPushButton(self.frm_left)
        self.btn_left.setObjectName("btn_left")
        self.gridLayout_4.addWidget(self.btn_left, 4, 0, 1, 1)
        self.btn_delete = QtWidgets.QPushButton(self.frm_left)
        self.btn_delete.setObjectName("btn_delete")
        self.gridLayout_4.addWidget(self.btn_delete, 3, 0, 1, 2)
        self.btn_export = QtWidgets.QPushButton(self.frm_left)
        self.btn_export.setObjectName("btn_export")
        self.gridLayout_4.addWidget(self.btn_export, 2, 0, 1, 2)
        self.lbl_ch = QtWidgets.QLabel(self.frm_left)
        self.lbl_ch.setMinimumSize(QtCore.QSize(93, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_ch.setFont(font)
        self.lbl_ch.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_ch.setObjectName("lbl_ch")
        self.gridLayout_4.addWidget(self.lbl_ch, 7, 0, 1, 2, QtCore.Qt.AlignHCenter)
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
        self.swgt_1.setCurrentIndex(0)
        self.swgt_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Prereg Planner"))
        self.lbl_kulliyah.setText(_translate("MainWindow", "Kulliyah"))
        self.lbl_session.setText(_translate("MainWindow", "Session"))
        self.lbl_type.setText(_translate("MainWindow", "Type"))
        self.btn_load_courses.setText(_translate("MainWindow", "Load courses"))
        self.lbl_or.setText(_translate("MainWindow", "or"))
        self.btn_open_file.setText(_translate("MainWindow", "Open file"))
        self.lbl_loaded_courses.setText(_translate("MainWindow", "Loaded courses"))
        self.lbl_search.setText(_translate("MainWindow", "Search"))
        self.lbl_selected_courses.setText(_translate("MainWindow", "Selected courses"))
        self.btn_generate.setText(_translate("MainWindow", "Generate Schedule"))
        self.btn_save.setText(_translate("MainWindow", "save"))
        self.lbl_index.setText(_translate("MainWindow", "? / ?"))
        self.btn_add.setText(_translate("MainWindow", "add"))
        self.btn_right.setText(_translate("MainWindow", ">"))
        self.btn_left.setText(_translate("MainWindow", "<"))
        self.btn_delete.setText(_translate("MainWindow", "delete"))
        self.btn_export.setText(_translate("MainWindow", "export"))
        self.lbl_ch.setText(_translate("MainWindow", "Total CH: ?"))

    def run(self):
        #************************IMPLEMENTATION************************#
        ############################ PAGE 1 ############################
        
        self.course_engine = CourseEngine()
        self.table_engine = TableEngine()

        self.cb_kulliyah.addItems(self.course_engine.getKulliyahs())
        self.cb_session.addItems(self.course_engine.getSessions())
        self.cb_type.addItems(['UNDERGRADUATE', 'POSTGRADUATE'])
        self.btn_load_courses.clicked.connect(self.btn_load_courses_clicked)
        self.btn_open_file.clicked.connect(self.btn_open_file_clicked)

        self.tb_search.textChanged.connect(self.tb_search_typed)
        self.twgt_loaded_courses.setTableType('select')
        self.btn_generate.clicked.connect(self.btn_generate_clicked)
        self.btn_generate.setDisabled(True)
        self.twgt_selected_courses.setTableType('deselect')

        ############################# PAGE 2 ############################
        self.ogl_table.setTableEngine(self.table_engine)
        self.btn_left.clicked.connect(self.btn_left_clicked)
        self.btn_right.clicked.connect(self.btn_right_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_export.clicked.connect(self.btn_export_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)

        # self.course_engine.loadCourses(7, 0, 0) # Loads Engin Kulliyah's Subjects
        # # ----------------------TEST 1---------------------- #  4th year subjects
        # # self.course_engine.selectCourse("ECIE 4101")
        # # self.course_engine.selectCourse("ECIE 4311")
        # # self.course_engine.selectCourse("ECIE 4312")
        # # self.course_engine.selectCourse("ECIE 4313")
        # # self.course_engine.selectCourse("ECIE 4351")
        # # self.course_engine.selectCourse("ECIE 4398")
        # # self.course_engine.selectCourse("EECE 3102")
        # # self.course_engine.selectCourse("MANU 3318")
        # # ----------------------TEST 2---------------------- #  1st year subjects
        # self.course_engine.selectCourse('EECE 1101')
        # self.course_engine.selectCourse('EECE 1312')
        # self.course_engine.selectCourse('EECE 1313')
        # self.course_engine.selectCourse('MATH 1320')
        # self.course_engine.selectCourse('MECH 1302')
        # self.course_engine.deselectCourse('EECE 1101')
        
        # vtblcourses = self.course_engine.getVTableCourses() # vector list of course tables
        # n_chs = self.course_engine.getCHs() # list of credit hours
        # b_selected_courses = [
        #     True,
        #     True,
        #     True,
        #     True,
        #     True,
        #     True,
        #     True,
        #     True,
        # ]
        # table_engine = TableEngine()
        # table_engine.setVTblCourses(vtblcourses, n_chs, b_selected_courses)
        
        # combinations = table_engine.getCombinations(self.ogl_table.width(), self.ogl_table.height())
        # self.ogl_table.setTableEngine(table_engine, self.btn_left, self.btn_right, self.lbl_index)
        # self.ogl_table.setCombinations(combinations)
    
    # HELPER METHODS
    def updateHiddenLoadedCourses(self):
        str_sub = self.tb_search.text().lower()
        ce = self.course_engine

        # check searched courses
        for code, course in ce.loaded_courses.items():
            index = course.index
            if str_sub:
                if str_sub in code.lower():
                    self.twgt_loaded_courses.showRow(index)
                else:
                    self.twgt_loaded_courses.hideRow(index)
            else:
                self.twgt_loaded_courses.showRow(index)
                    
        # check selected courses
        for code, course in ce.selected_courses.items():
            if code in ce.loaded_courses and course.param == ce.current_param:
                index = ce.loaded_courses[code].index
                self.twgt_loaded_courses.hideRow(index)

    # WIDGET EVENTS
    def btn_load_courses_clicked(self):
        n1 = self.cb_kulliyah.currentIndex()
        n2 = self.cb_session.currentIndex()
        n3 = self.cb_type.currentIndex()

        ce = self.course_engine
        ce.loadCourses(n1, n2, n3)
        self.twgt_loaded_courses.setRowCount(0)
        for code in ce.loaded_courses.keys():
            def rtnlambda(c):
                return lambda: self.btn_add_course_clicked(c)
            self.twgt_loaded_courses.addItem(code, ce.loaded_courses[code].title, "+", rtnlambda(code))

        self.updateHiddenLoadedCourses()

    def btn_open_file_clicked(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open session", "", "DAT file (*.dat)")
        if file:
            ce = self.course_engine
            ce.readFile(file)
            for code in ce.selected_courses.keys():
                if len(ce.selected_courses) >= 2:
                    self.btn_generate.setDisabled(False)
                def rtnLambda(c):
                    return lambda: self.btn_remove_course_clicked(c)
                self.twgt_selected_courses.addItem(code, ce.selected_courses[code].title, "-", rtnLambda(code))
            self.btn_generate_clicked()

    def btn_add_course_clicked(self, code):
        ce = self.course_engine
        ce.selectCourse(code)
        if len(ce.selected_courses) >= 2:
            self.btn_generate.setDisabled(False)
        def rtnLambda(c):
            return lambda: self.btn_remove_course_clicked(c)
        self.twgt_selected_courses.addItem(code, ce.selected_courses[code].title, "-", rtnLambda(code))
        self.twgt_loaded_courses.hideRow(ce.selected_courses[code].index)

    def btn_remove_course_clicked(self, code):
        ce = self.course_engine
        self.twgt_selected_courses.removeRow(list(ce.selected_courses).index(code))
        ce.deselectCourse(code)
        if len(ce.selected_courses) < 2:
            self.btn_generate.setDisabled(True)
        self.updateHiddenLoadedCourses()

    def tb_search_typed(self):
        self.updateHiddenLoadedCourses()

    def btn_generate_clicked(self):
        vtblcourses = self.course_engine.getVTableCourses() # vector list of course tables
        n_chs = self.course_engine.getCHs() # list of credit hours

        self.table_engine.setVTblCourses(vtblcourses, n_chs)
        self.ogl_table.updateCombinations(0)

        self.lbl_index.setText(f"{self.table_engine.index + 1} / {self.table_engine.getVCombinationsSize()}")
        self.lbl_ch.setText(f'Total CH: {self.table_engine.getTotalCH()}')

        self.swgt_1.setCurrentIndex(1)

    def btn_left_clicked(self):
        index = self.table_engine.index - 1
        if index >= 0:
            self.ogl_table.updateCombinations(index)
            self.ogl_table.paintGL()
            self.lbl_index.setText(f"{index + 1} / {self.table_engine.getVCombinationsSize()}")

    def btn_right_clicked(self):
        index = self.table_engine.index + 1
        if index < self.table_engine.getVCombinationsSize():
            self.ogl_table.updateCombinations(index)
            self.ogl_table.paintGL()
            self.lbl_index.setText(f"{index + 1} / {self.table_engine.getVCombinationsSize()}")

    def btn_add_clicked(self):
        self.ogl_table.clear()
        self.table_engine.clear()
        self.swgt_1.setCurrentIndex(0)

    def btn_save_clicked(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save session", "session", "DAT file (*.dat)")
        if file:
            self.course_engine.writeFile(file)

    def btn_export_clicked(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save as...", "table", "PNG (*.png);; BMP (*.bmp);;TIFF (*.tiff *.tif);; JPEG (*.jpg *.jpeg)")
        if file:
            image = QtGui.QImage(self.ogl_table.grab())
            image.save(file)

    def btn_delete_clicked(self):
        self.ogl_table.clear()
        self.table_engine.clear()
        self.twgt_loaded_courses.setRowCount(0)
        self.twgt_selected_courses.setRowCount(0)
        self.course_engine.clear()
        self.tb_search.setText('')
        self.btn_generate.setDisabled(True)
        self.swgt_1.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.run()
    MainWindow.show()
    sys.exit(app.exec_())
