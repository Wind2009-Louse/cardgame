# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\temp\py\cardgame\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(446, 497)
        self.centralwidget = QtWidgets.QWidget(self)

        self.centralwidget.setObjectName("centralwidget")
        self.username_input = QtWidgets.QLineEdit(self.centralwidget)
        self.username_input.setGeometry(QtCore.QRect(100, 20, 331, 31))
        self.username_input.setObjectName("username_input")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 72, 15))
        self.label_2.setObjectName("label_2")
        self.password_input = QtWidgets.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(100, 60, 331, 31))
        self.password_input.setObjectName("password_input")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(20, 171, 401, 301))
        self.listView.setObjectName("listView")

        self.port_input = QtWidgets.QLineEdit(self.centralwidget)
        self.port_input.setGeometry(QtCore.QRect(340, 100, 91, 31))
        self.port_input.setObjectName("port_input")
        regx = QtCore.QRegExp("^[0-9]{5}$")# 
        validator = QtGui.QRegExpValidator(regx, self.port_input)
        self.port_input.setValidator(validator)

        self.ip_input = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.ip_input.setGeometry(QtCore.QRect(100, 100, 171, 31))
        self.ip_input.setObjectName("ip_input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 110, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 110, 51, 16))
        self.label_4.setObjectName("label_4")
        self.connect_button = QtWidgets.QPushButton(self.centralwidget)
        self.connect_button.setGeometry(QtCore.QRect(30, 140, 190, 28))
        self.connect_button.setObjectName("connect_button")

        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(240, 140, 191, 28))
        self.create_button.setObjectName("create_button")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "主界面"))
        self.label.setText(_translate("MainWindow", "用户名"))
        self.label_2.setText(_translate("MainWindow", "密码(可选)"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.label_4.setText(_translate("MainWindow", "服务器"))
        self.connect_button.setText(_translate("MainWindow", "连接服务器"))
        self.create_button.setText(_translate("MainWindow", "创建房间"))
