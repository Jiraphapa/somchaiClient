# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/assignForm.ui'
#
# Created: Mon Apr 25 19:27:00 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(373, 343)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 0, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.employeeLabel = QtWidgets.QLabel(Form)
        self.employeeLabel.setStyleSheet("color:white;")
        self.employeeLabel.setGeometry(QtCore.QRect(30, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.employeeLabel.setFont(font)
        self.employeeLabel.setObjectName("employeeLabel")
        self.taskLabel = QtWidgets.QLabel(Form)
        self.taskLabel.setStyleSheet("color:white;")
        self.taskLabel.setGeometry(QtCore.QRect(30, 110, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.taskLabel.setFont(font)
        self.taskLabel.setObjectName("taskLabel")
        self.deadlineLabel = QtWidgets.QLabel(Form)
        self.deadlineLabel.setStyleSheet("color:white;")
        self.deadlineLabel.setGeometry(QtCore.QRect(30, 220, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.deadlineLabel.setFont(font)
        self.deadlineLabel.setObjectName("deadlineLabel")
        self.employeeBox = QtWidgets.QComboBox(Form)
        self.employeeBox.setStyleSheet("color:white;background-color:#121317;")
        self.employeeBox.setGeometry(QtCore.QRect(150, 70, 191, 31))
        self.employeeBox.setObjectName("employeeBox")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setStyleSheet("color:white;background-color:#121317;")
        self.dateTimeEdit.setGeometry(QtCore.QRect(140, 190, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.assignButton = QtWidgets.QPushButton(Form)
        self.assignButton.setStyleSheet("color:white;background-color:#121317;")
        self.assignButton.setGeometry(QtCore.QRect(130, 270, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.assignButton.setFont(font)
        self.assignButton.setObjectName("assignButton")
        self.descripEdit = QtWidgets.QTextEdit(Form)
        self.descripEdit.setGeometry(QtCore.QRect(190, 110, 151, 61))
        self.descripEdit.setObjectName("descripEdit")
        self.descripEdit.setStyleSheet("color:white;background-color:#121317;")
        self.startLabel = QtWidgets.QLabel(Form)
        self.startLabel.setGeometry(QtCore.QRect(30, 180, 91, 41))
        self.startLabel.setStyleSheet("color:white;")
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.startLabel.setFont(font)
        self.startLabel.setObjectName("startLabel")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setStyleSheet("color:white;background-color:#121317;")
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(140, 230, 194, 24))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ASSIGN TASK"))
        self.employeeLabel.setText(_translate("Form", "Employee"))
        self.taskLabel.setText(_translate("Form", "Task description"))
        self.deadlineLabel.setText(_translate("Form", "Deadline"))
        self.assignButton.setText(_translate("Form", "ASSIGN"))
        self.startLabel.setText(_translate("Form", "Start date"))

