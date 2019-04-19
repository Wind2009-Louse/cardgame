# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\temp\py\cardgame\ui_file\room.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import threading

class flush_thread(threading.Thread):
    def __init__(self, window):
        super().__init__()
        self.window = window
    def run(self):
        while(self.window.alive):
            data = self.window.pack_socket.recv_msg(["update"],b=False)
            if data is not None:
                self.window.port.setText("端口: %d"%data["port"])
                self.window.user_1.setText(data["names"][0])
                if len(data["names"]) > 1:
                    self.window.user_2.setText(data["names"][1])
                if data["ready"]:
                    self.window.ReadyButton.setText("取消准备")
                else:
                    self.window.ReadyButton.setText("准备")
                if data["id"] == 1:
                    self.window.ReadyButton.setEnabled(True)
                if data["id"] == 0 and data["ready"]:
                    self.window.StartButton.setEnabled(True)

class Ui_RoomWindow(QtWidgets.QWidget):
    def __init__(self, pack_socket):
        super(Ui_RoomWindow, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(416, 248)
        self.centralwidget = QtWidgets.QWidget(self)

        self.centralwidget.setObjectName("centralwidget")
        self.user_1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.user_1.setGeometry(QtCore.QRect(20, 70, 271, 51))
        self.user_1.setObjectName("user_1")
        self.user_1.setEnabled(False)
        self.user_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.user_2.setGeometry(QtCore.QRect(20, 150, 271, 51))
        self.user_2.setObjectName("user_2")
        self.user_2.setEnabled(False)
        self.port = QtWidgets.QTextBrowser(self.centralwidget)
        self.port.setGeometry(QtCore.QRect(20, 20, 271, 31))
        self.port.setObjectName("port")
        self.port.setEnabled(False)
        self.ReadyButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReadyButton.setGeometry(QtCore.QRect(310, 160, 93, 28))
        self.ReadyButton.setObjectName("Ready")
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(310, 80, 93, 28))
        self.StartButton.setObjectName("Begin")
        self.ReadyButton.setEnabled(False)
        self.StartButton.setEnabled(False)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pack_socket = pack_socket
        self.alive = True
        update_p = flush_thread(self)
        update_p.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "房间"))
        self.ReadyButton.setText(_translate("MainWindow", "准备"))
        self.StartButton.setText(_translate("MainWindow", "开始"))

    def closeEvent(self, event):
        self.parent.show()