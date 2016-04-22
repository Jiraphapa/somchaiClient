# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 308)
        Form.setMaximumSize(QtCore.QSize(476, 308))
        self.header_label = QtGui.QLabel(Form)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        self.header_label.setFont(font)
        self.header_label.setFrameShape(QtGui.QFrame.NoFrame)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.help = QtGui.QLabel(Form)
        self.help.setGeometry(QtCore.QRect(10, 60, 451, 231))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.help.setFont(font)
        self.help.setTextFormat(QtCore.Qt.AutoText)
        self.help.setScaledContents(False)
        self.help.setWordWrap(True)
        self.help.setObjectName("help")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.header_label.setText(_translate("Form", "Help"))
        self.help.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et magna tincidunt, pharetra sapien at, pulvinar magna. In egestas, turpis dignissim feugiat vestibulum, augue lectus placerat augue, non fringilla nulla ligula sed ipsum. Duis non consequat diam, nec blandit nisi. Donec vestibulum volutpat nisl eu dignissim. Donec ut euismod neque. Vivamus et nibh sit amet ante ultrices cursus sit amet et mauris. Etiam porttitor lorem ac euismod posuere. Sed vel volutpat felis. Praesent sit amet molestie erat, nec mattis dui. Etiam in eleifend ex. "))

