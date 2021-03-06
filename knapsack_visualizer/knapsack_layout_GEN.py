# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'knapsack_layout.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(991, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.alg_box = QtWidgets.QComboBox(self.centralwidget)
        self.alg_box.setObjectName("alg_box")
        self.horizontalLayout_6.addWidget(self.alg_box)
        self.alg_btn = QtWidgets.QPushButton(self.centralwidget)
        self.alg_btn.setObjectName("alg_btn")
        self.horizontalLayout_6.addWidget(self.alg_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.status_lbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.status_lbl.setFont(font)
        self.status_lbl.setObjectName("status_lbl")
        self.verticalLayout.addWidget(self.status_lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_sol_btn = QtWidgets.QPushButton(self.centralwidget)
        self.show_sol_btn.setObjectName("show_sol_btn")
        self.horizontalLayout.addWidget(self.show_sol_btn)
        self.cleardp_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cleardp_btn.setObjectName("cleardp_btn")
        self.horizontalLayout.addWidget(self.cleardp_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.dp_table = DPQTableWidget(self.centralwidget)
        self.dp_table.setObjectName("dp_table")
        self.dp_table.setColumnCount(0)
        self.dp_table.setRowCount(0)
        self.verticalLayout.addWidget(self.dp_table)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.step_back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.step_back_btn.setObjectName("step_back_btn")
        self.horizontalLayout_2.addWidget(self.step_back_btn)
        self.pause_btn = QtWidgets.QPushButton(self.centralwidget)
        self.pause_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/play-line.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause_btn.setIcon(icon)
        self.pause_btn.setObjectName("pause_btn")
        self.horizontalLayout_2.addWidget(self.pause_btn)
        self.speed_slider = QtWidgets.QSlider(self.centralwidget)
        self.speed_slider.setMaximumSize(QtCore.QSize(797, 16777215))
        self.speed_slider.setMinimum(1)
        self.speed_slider.setMaximum(30)
        self.speed_slider.setSingleStep(4)
        self.speed_slider.setPageStep(4)
        self.speed_slider.setProperty("value", 1)
        self.speed_slider.setSliderPosition(1)
        self.speed_slider.setOrientation(QtCore.Qt.Horizontal)
        self.speed_slider.setObjectName("speed_slider")
        self.horizontalLayout_2.addWidget(self.speed_slider)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 991, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KnapSack Visualizer"))
        self.label.setText(_translate("MainWindow", "Choose your algorithm: "))
        self.alg_btn.setText(_translate("MainWindow", "Click To Solve."))
        self.label_2.setText(_translate("MainWindow", "NOTE: Use Arrow Keys to move around table. Mouse clicks are ignored when visualizing the solutions."))
        self.status_lbl.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#fc0000;\">Status: Not Ready (Choose an algorithm Above)</span></p></body></html>"))
        self.show_sol_btn.setText(_translate("MainWindow", "Show Solution"))
        self.cleardp_btn.setText(_translate("MainWindow", "Clear Solution"))
        self.step_back_btn.setText(_translate("MainWindow", "Step Back"))
        self.speed_slider.setToolTip(_translate("MainWindow", "Speed"))
from dpqtablewidget import DPQTableWidget
