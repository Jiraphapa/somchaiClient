# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 308)
        Form.setMaximumSize(QtCore.QSize(476, 308))
        self.header_label = QtWidgets.QLabel(Form)
        self.header_label.setGeometry(QtCore.QRect(0, 0, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(50)
        self.header_label.setFont(font)
        self.header_label.setStyleSheet("color:white;")
        self.header_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.header_label.setObjectName("header_label")
        self.help = QtWidgets.QLabel(Form)
        self.help.setGeometry(QtCore.QRect(10, 60, 451, 231))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.help.setFont(font)
        self.help.setStyleSheet("background-color:white;color:#121317;")
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
        #self.help.setText(_translate("Form", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut et magna tincidunt, pharetra sapien at, pulvinar magna. In egestas, turpis dignissim feugiat vestibulum, augue lectus placerat augue, non fringilla nulla ligula sed ipsum. Duis non consequat diam, nec blandit nisi. Donec vestibulum volutpat nisl eu dignissim. Donec ut euismod neque. Vivamus et nibh sit amet ante ultrices cursus sit amet et mauris. Etiam porttitor lorem ac euismod posuere. Sed vel volutpat felis. Praesent sit amet molestie erat, nec mattis dui. Etiam in eleifend ex. "))
        self.help.setText(_translate("Form", "Somchai is a human­like office assistant software where user can communicate in office in an easy way by asking Somchai to do the following tasks\n"
"\n"
"‘Todo’ provides a list of tasks assigned by the manager or employee himself/herself , you can view the full tasks , add or mark finished task by clicking on its area.\n"
"‘Chat’ provides a feature for manager to create a chatroom which any employee or manager in the company to join and a feature to join the chat room if there exists any\n"
"‘Reserve’ provides you features to display the available conference room and to reserve if the room is available\n"
"‘Profile’ provides all the information of user , manager can view all the information of employee"))
