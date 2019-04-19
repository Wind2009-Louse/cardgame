# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\temp\py\cardgame\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import server
import room
import socketlib

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

        self.ip_input = QtWidgets.QLineEdit(self.centralwidget)
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
        self.connect_button.clicked.connect(self.join_server)

        self.create_button = QtWidgets.QPushButton(self.centralwidget)
        self.create_button.setGeometry(QtCore.QRect(240, 140, 191, 28))
        self.create_button.setObjectName("create_button")
        self.create_button.clicked.connect(self.create_server)

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

    def create_server(self):
        srv = server.Game_server()
        srv.start()
        self.connect_to_server("127.0.0.1", srv.port)
    
    def join_server(self):
        ip_addr = self.ip_input.text()
        port_str = self.port_input.text()
        if not port_str.isalnum() or len(port_str) == 0:
            QtWidgets.QMessageBox.warning(self, "错误", "端口错误", QtWidgets.QMessageBox.Yes)
            return
        port_num = int(port_str)
        self.connect_to_server(ip_addr, port_num)
    
    def connect_to_server(self, ip_addr, port_num):
        self.connect_button.setEnabled(False)
        self.create_button.setEnabled(False)
        try:
            user_name = self.username_input.text()
            toserver_sck = socketlib.packed_client(ip_addr, port_num, tout=10)
            toserver_sck.send_msg({"type":"request", "name":user_name})
            if toserver_sck.recv_msg(["accpet"]):
                self.connect_button.setEnabled(True)
                self.create_button.setEnabled(True)
                self.hide()
                self.new_ui = room.Ui_RoomWindow(toserver_sck)
                self.new_ui.parent = self
                self.new_ui.show()
        except:
            QtWidgets.QMessageBox.warning(self, "错误", "无法连接到服务器", QtWidgets.QMessageBox.Yes)
            self.connect_button.setEnabled(True)
            self.create_button.setEnabled(True)