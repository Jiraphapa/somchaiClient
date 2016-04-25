# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/reserveForm.ui'
#
# Created: Mon Apr 25 13:21:57 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 253)
        self.topicEdit = QtGui.QLineEdit(Form)
        self.topicEdit.setGeometry(QtCore.QRect(110, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.topicEdit.setFont(font)
        self.topicEdit.setObjectName("topicEdit")
        self.topicLabel = QtGui.QLabel(Form)
        self.topicLabel.setGeometry(QtCore.QRect(20, 40, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.topicLabel.setFont(font)
        self.topicLabel.setObjectName("topicLabel")
        self.datetimeLabel = QtGui.QLabel(Form)
        self.datetimeLabel.setGeometry(QtCore.QRect(20, 90, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.datetimeLabel.setFont(font)
        self.datetimeLabel.setObjectName("datetimeLabel")
        self.dateTimeEdit = QtGui.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(180, 90, 141, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.reserveButton = QtGui.QPushButton(Form)
        self.reserveButton.setGeometry(QtCore.QRect(120, 140, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.reserveButton.setFont(font)
        self.reserveButton.setObjectName("reserveButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.topicLabel.setText(QtGui.QApplication.translate("Form", "Topic", None, QtGui.QApplication.UnicodeUTF8))
        self.datetimeLabel.setText(QtGui.QApplication.translate("Form", "Date & Time", None, QtGui.QApplication.UnicodeUTF8))
        self.reserveButton.setText(QtGui.QApplication.translate("Form", "RESERVE", None, QtGui.QApplication.UnicodeUTF8))

