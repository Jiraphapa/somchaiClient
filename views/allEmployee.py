# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/allEmployee.ui'
#
# Created: Thu May 19 22:53:19 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(231, 268)
        self.employee_label = QtWidgets.QLabel(Form)
        self.employee_label.setGeometry(QtCore.QRect(20, 20, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.employee_label.setFont(font)
        self.employee_label.setObjectName("employee_label")
        self.employeeList = QtWidgets.QListWidget(Form)
        self.employeeList.setGeometry(QtCore.QRect(10, 60, 211, 192))
        self.employeeList.setObjectName("employeeList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.employee_label.setText(_translate("Form", "EMPLOYEE LIST"))

