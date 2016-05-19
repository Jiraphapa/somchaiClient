# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/reserveShow.ui'
#
# Created: Mon Apr 25 13:05:25 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(344, 374)
        self.reserve_label = QtWidgets.QLabel(Form)
        self.reserve_label.setGeometry(QtCore.QRect(30, 20, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.reserve_label.setFont(font)
        self.reserve_label.setStyleSheet("color:#f8e71d;")
        self.reserve_label.setObjectName("reserve_label")
        self.reserved_list = QtWidgets.QListWidget(Form)
        self.reserved_list.setStyleSheet("background-color:#23252c;")
        self.reserved_list.setGeometry(QtCore.QRect(20, 70, 301, 221))
        self.reserved_list.setObjectName("reserved_list")
        self.reserveButton = QtWidgets.QPushButton(Form)
        self.reserveButton.setStyleSheet("background-color:#f8e71d;")
        self.reserveButton.setGeometry(QtCore.QRect(20, 310, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.reserveButton.setFont(font)
        self.reserveButton.setObjectName("reserveButton")
        self.cancelButton = QtWidgets.QPushButton(Form)
        self.cancelButton.setStyleSheet("color:#f8e71d;")
        self.cancelButton.setGeometry(QtCore.QRect(180, 310, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.cancelButton.setFont(font)
        self.cancelButton.setObjectName("cancelButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reserve_label.setText(_translate("Form", "RESERVED LIST"))
        self.reserveButton.setText(_translate("Form", "RESERVE"))
        self.cancelButton.setText(_translate("Form", "REMOVE"))

