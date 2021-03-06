# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Downloads/Sample-Ui_V2/reserveForm.ui'
#
# Created: Mon Apr 25 15:25:37 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(340, 353)
        self.topicEdit = QtWidgets.QLineEdit(Form)
        self.topicEdit.setGeometry(QtCore.QRect(110, 20, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(18)
        font.setWeight(50)
        font.setBold(False)
        self.topicEdit.setFont(font)
        self.topicEdit.setStyleSheet("background-color:#121317;color:white;")
        self.topicEdit.setObjectName("topicEdit")
        self.topicLabel = QtWidgets.QLabel(Form)
        self.topicLabel.setGeometry(QtCore.QRect(20, 30, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.topicLabel.setFont(font)
        self.topicLabel.setObjectName("topicLabel")
        self.datetimeLabel = QtWidgets.QLabel(Form)
        self.datetimeLabel.setGeometry(QtCore.QRect(20, 80, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)

        self.datetimeLabel.setFont(font)
        self.datetimeLabel.setObjectName("datetimeLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit.setStyleSheet("background-color:#121317;color:white;")
        self.dateTimeEdit.setGeometry(QtCore.QRect(180, 80, 141, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.reserveButton = QtWidgets.QPushButton(Form)
        self.reserveButton.setStyleSheet("background-color:#121317;color:white;")
        self.reserveButton.setGeometry(QtCore.QRect(60, 280, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(32)
        font.setWeight(75)
        font.setBold(True)
        self.reserveButton.setFont(font)
        self.reserveButton.setObjectName("reserveButton")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setDisplayFormat("yyyy-MM-dd hh:mm:ss")
        self.dateTimeEdit_2.setStyleSheet("background-color:#121317;color:white;")
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(180, 140, 141, 24))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 110, 56, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.room_label = QtWidgets.QLabel(Form)
        self.room_label.setGeometry(QtCore.QRect(20, 180, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setWeight(75)
        font.setBold(True)
        self.room_label.setFont(font)
        self.room_label.setObjectName("room_label")
        self.roomList = QtWidgets.QListWidget(Form)
        self.roomList.setGeometry(QtCore.QRect(110, 180, 191, 81))
        self.roomList.setObjectName("roomList")
        self.roomList.setStyleSheet("background-color:#121317;color:white;")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.topicLabel.setText(_translate("Form", "Topic"))
        self.datetimeLabel.setText(_translate("Form", "Date & Time"))
        self.reserveButton.setText(_translate("Form", "RESERVE"))
        self.label.setText(_translate("Form", "TO"))
        self.room_label.setText(_translate("Form", "Room"))

