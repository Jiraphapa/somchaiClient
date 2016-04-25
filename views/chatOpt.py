# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/chatOpt.ui'
#
# Created: Sun Apr 24 02:02:58 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 192)
        self.createButton = QtGui.QPushButton(Form)
        self.createButton.setGeometry(QtCore.QRect(10, 10, 171, 171))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(33)
        font.setWeight(75)
        font.setBold(True)
        self.createButton.setFont(font)
        self.createButton.setStyleSheet("background-color:#fe3d50;color:white;")
        self.createButton.setObjectName("createButton")
        self.joinButton = QtGui.QPushButton(Form)
        self.joinButton.setStyleSheet("background-color:white;color:#121317;")
        self.joinButton.setGeometry(QtCore.QRect(190, 10, 171, 171))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(33)
        font.setWeight(75)
        font.setBold(True)
        self.joinButton.setFont(font)
        self.joinButton.setObjectName("joinButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.createButton.setText(QtGui.QApplication.translate("Form", "CREATE", None, QtGui.QApplication.UnicodeUTF8))
        self.joinButton.setText(QtGui.QApplication.translate("Form", "JOIN", None, QtGui.QApplication.UnicodeUTF8))

