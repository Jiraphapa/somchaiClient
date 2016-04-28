# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import Connector
import urllib
import sys
import json

class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(271, 223)
        self.login = QtWidgets.QPushButton(Form)
        self.login.setDefault(True)
        self.login.setStyleSheet("background-color:#ffd200;")

        self.login.setGeometry(QtCore.QRect(80, 150, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.user_entry = QtWidgets.QLineEdit(Form)
        self.user_entry.setStyleSheet("background-color:#23252c;color:white;")
        self.user_entry.setGeometry(QtCore.QRect(80, 60, 161, 21))
        self.user_entry.setObjectName("user_entry")
        self.pass_entry = QtWidgets.QLineEdit(Form)
        self.pass_entry.setStyleSheet("background-color:#23252c;color:white;")
        self.pass_entry.setGeometry(QtCore.QRect(80, 100, 161, 21))
        self.pass_entry.setObjectName("pass_entry")
        self.pass_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        #hiding
        self.pass_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        self.username = QtWidgets.QLabel(Form)
        self.username.setStyleSheet("color:white;")
        self.username.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(Form)
        self.password.setStyleSheet("color:white;")
        self.password.setGeometry(QtCore.QRect(10, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.title = QtWidgets.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(0, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(16)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login.setText(_translate("Form", "Login"))
        self.username.setText(_translate("Form", "Username"))
        self.password.setText(_translate("Form", "Password"))
        self.title.setText(_translate("Form", "SOMCHAI SECRETARY APP"))
        self.title.setStyleSheet("color:white;")







