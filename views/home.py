
from PySide import QtCore, QtGui
from connector import *
import  urllib
import sys


import sys
import time


class Home(object):
    def setupUi(self, Form):
        self.num = 0

        Form.setObjectName("Form")
        Form.resize(609, 448)
        Form.setMaximumSize(QtCore.QSize(609, 448))
        self.todo_button = QtGui.QPushButton(Form)
        self.todo_button.setGeometry(QtCore.QRect(10, 240, 181, 181))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(40)
        self.todo_button.setFont(font)
        self.todo_button.setStyleSheet("background-color:#2283f6;")
        self.todo_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.todo_button.setText("")
        self.todo_button.setObjectName("todo_button")
        self.chat_button = QtGui.QPushButton(Form)
        self.chat_button.setGeometry(QtCore.QRect(200, 240, 181, 181))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        self.chat_button.setFont(font)
        self.chat_button.setStyleSheet("color:white;background-color:#fe3d50;")
        self.chat_button.setObjectName("chat_button")
        self.reserve_button = QtGui.QPushButton(Form)
        self.reserve_button.setStyleSheet("color:white;")
        self.reserve_button.setGeometry(QtCore.QRect(390, 240, 181, 181))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(35)
        self.reserve_button.setFont(font)
        self.reserve_button.setStyleSheet("background-color:#f8e71d;color:#464646;")
        self.reserve_button.setObjectName("reserve_button")
        self.profile_button = QtGui.QPushButton(Form)
        self.profile_button.setStyleSheet("color:white;background-color:#01cc9f;")
        self.profile_button.setGeometry(QtCore.QRect(490, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.profile_button.setFont(font)
        self.profile_button.setObjectName("profile_button")
        self.help_button = QtGui.QPushButton(Form)
        self.help_button.setGeometry(QtCore.QRect(400, 0, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.help_button.setFont(font)
        self.help_button.setStyleSheet("color:white;background-color:#244856;")
        self.help_button.setObjectName("help_button")
        self.time_label = QtGui.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(140, 70, 331, 111))
        #140, 70, 331, 111
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(85)
        self.time_label.setFont(font)
        self.time_label.setStyleSheet("color:white;")
        self.time_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.todo_label = QtGui.QLabel(Form)
        self.todo_label.setGeometry(QtCore.QRect(10, 240, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(40)
        self.todo_label.setStyleSheet("color:white;background-color:#2283f6;")
        self.todo_label.setFont(font)
        self.todo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_label.setObjectName("todo_label")
        self.list_widget = QtGui.QListWidget(Form)
        self.list_widget.setGeometry(QtCore.QRect(20, 280, 161, 131))
        self.list_widget.setObjectName("list_widget")
        # self.background_inner = QtGui.QLabel(Form)
        # self.background_inner.setGeometry(QtCore.QRect(0, 40, 581, 171))
        # self.background_inner.setFrameShape(QtGui.QFrame.WinPanel)
        # self.background_inner.setText("")
        # self.background_inner.setObjectName("background_inner")
        # self.background_out = QtGui.QLabel(Form)
        # self.background_out.setGeometry(QtCore.QRect(0, 30, 581, 191))
        # self.background_out.setFrameShape(QtGui.QFrame.WinPanel)
        # self.background_out.setText("")
        # self.background_out.setObjectName("background_out")
        # self.background_out.raise_()
        # self.background_inner.raise_()
        self.todo_button.raise_()
        self.chat_button.raise_()
        self.reserve_button.raise_()
        self.profile_button.raise_()
        self.help_button.raise_()
        self.time_label.raise_()
        self.todo_label.raise_()
        self.list_widget.raise_()

        #DigitalClock
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_value)
        self.timer.start(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chat_button.setText(_translate("Form", "CHAT"))
        self.reserve_button.setText(_translate("Form", "RESERVE"))
        self.profile_button.setText(_translate("Form", "Profile"))
        self.help_button.setText(_translate("Form", "Help"))
        #self.time_label.setText(_translate("Form", "Time"))
        self.todo_label.setText(_translate("Form", "Todo"))

    def update_value(self):
        self.num += 1
        if self.num > 100:
            self.num = 0
        self.time_label.setText(time.strftime("%X"))









def main():

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    ex = Home()
    ex.setupUi(w)
    w.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())
