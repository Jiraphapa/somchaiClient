# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/chatRoom.ui'
#
# Created: Sun Apr 24 16:35:12 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(445, 430)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        Form.setFont(font)
        self.messageEdit = QtGui.QLineEdit(Form)
        self.messageEdit.setGeometry(QtCore.QRect(180, 370, 241, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(50)
        font.setBold(False)
        self.messageEdit.setFont(font)
        self.messageEdit.setText("")
        self.messageEdit.setObjectName("messageEdit")
        self.onlineList = QtGui.QListWidget(Form)
        self.onlineList.setStyleSheet("background-color:#23252c;")
        self.onlineList.setGeometry(QtCore.QRect(20, 70, 151, 341))
        self.onlineList.setObjectName("onlineList")
        self.messageList = QtGui.QListView(Form)
        self.messageList.setStyleSheet("background-color:#23252c;")
        self.messageEdit.setStyleSheet("background-color:white;")
        self.messageList.setGeometry(QtCore.QRect(180, 20, 241, 341))
        self.messageList.setObjectName("messageList")
        self.online_label = QtGui.QLabel(Form)
        self.online_label.setGeometry(QtCore.QRect(30, 10, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.online_label.setFont(font)
        self.online_label.setStyleSheet("color:white;")
        self.online_label.setObjectName("online_label")
        self.contact_label = QtGui.QLabel(Form)
        self.contact_label.setStyleSheet("color:white;")
        self.contact_label.setGeometry(QtCore.QRect(40, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.contact_label.setFont(font)
        self.contact_label.setObjectName("contact_label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.online_label.setText(QtGui.QApplication.translate("Form", "ONLINE", None, QtGui.QApplication.UnicodeUTF8))
        self.contact_label.setText(QtGui.QApplication.translate("Form", "CONTACT", None, QtGui.QApplication.UnicodeUTF8))

