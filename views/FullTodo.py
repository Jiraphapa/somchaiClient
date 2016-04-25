# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/FullTodo.ui'
#
# Created: Sun Apr 24 23:16:06 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(302, 530)
        self.todoList_label = QtGui.QLabel(Form)
        self.todoList_label.setGeometry(QtCore.QRect(60, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        font.setWeight(75)
        font.setBold(True)
        self.todoList_label.setFont(font)
        self.todoList_label.setStyleSheet("color:white;")
        self.todoList_label.setObjectName("todoList_label")
        self.tasksList = QtGui.QListWidget(Form)
        self.tasksList.setGeometry(QtCore.QRect(15, 70, 271, 361))
        self.tasksList.setStyleSheet("background-color:white;")
        self.tasksList.setObjectName("tasksList")
        self.addButton = QtGui.QPushButton(Form)
        self.addButton.setGeometry(QtCore.QRect(10, 440, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.finishButton = QtGui.QPushButton(Form)
        self.finishButton.setGeometry(QtCore.QRect(160, 440, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.finishButton.setFont(font)
        self.finishButton.setObjectName("finishButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.todoList_label.setText(QtGui.QApplication.translate("Form", "TODO LIST", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setText(QtGui.QApplication.translate("Form", "ADD", None, QtGui.QApplication.UnicodeUTF8))
        self.finishButton.setText(QtGui.QApplication.translate("Form", "FINISH", None, QtGui.QApplication.UnicodeUTF8))

