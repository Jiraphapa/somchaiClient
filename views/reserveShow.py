# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/reserveShow.ui'
#
# Created: Mon Apr 25 13:05:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 367)
        self.reserve_label = QtGui.QLabel(Form)
        self.reserve_label.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.reserve_label.setFont(font)
        self.reserve_label.setObjectName("reserve_label")
        self.reserved_list = QtGui.QListWidget(Form)
        self.reserved_list.setGeometry(QtCore.QRect(20, 70, 301, 221))
        self.reserved_list.setObjectName("reserved_list")
        self.reserveButton = QtGui.QPushButton(Form)
        self.reserveButton.setGeometry(QtCore.QRect(70, 300, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.reserveButton.setFont(font)
        self.reserveButton.setObjectName("reserveButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.reserve_label.setText(QtGui.QApplication.translate("Form", "RESERVED LIST", None, QtGui.QApplication.UnicodeUTF8))
        self.reserveButton.setText(QtGui.QApplication.translate("Form", "RESERVE A ROOM", None, QtGui.QApplication.UnicodeUTF8))

