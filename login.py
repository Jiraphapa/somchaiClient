# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import connector
import  urllib
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(271, 223)
        self.login = QtGui.QPushButton(Form)
        self.login.clicked.connect(self.doLogin)
        self.login.setGeometry(QtCore.QRect(80, 140, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.login.setFont(font)
        self.login.setObjectName("login")
        self.user_entry = QtGui.QLineEdit(Form)
        self.user_entry.setGeometry(QtCore.QRect(80, 60, 161, 21))
        self.user_entry.setObjectName("user_entry")
        self.pass_entry = QtGui.QLineEdit(Form)
        self.pass_entry.setGeometry(QtCore.QRect(80, 100, 161, 21))
        self.pass_entry.setObjectName("pass_entry")
        self.username = QtGui.QLabel(Form)
        self.username.setGeometry(QtCore.QRect(10, 60, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.username.setFont(font)
        self.username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setObjectName("username")
        self.password = QtGui.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(10, 100, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.password.setFont(font)
        self.password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.register_2 = QtGui.QPushButton(Form)
        self.register_2.clicked.connect(self.doRegister)
        self.register_2.setGeometry(QtCore.QRect(80, 180, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.register_2.setFont(font)
        self.register_2.setObjectName("register_2")
        self.title = QtGui.QLabel(Form)
        self.title.setGeometry(QtCore.QRect(0, 10, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login.setText(_translate("Form", "Login"))
        self.username.setText(_translate("Form", "Username"))
        self.password.setText(_translate("Form", "Password"))
        self.register_2.setText(_translate("Form", "Register"))
        self.title.setText(_translate("Form", "SomChai Secretary App"))

    def doLogin(self):
        usrname=self.user_entry.text()
        psw=self.password.text()
        #authenticate
        data= {'username': usrname,'password': psw,}
        url="http://127.0.0.1:8001/v1/auth/login"
        connector.post(data,url)


    def doRegister(self):
        #redirect to register page
        pass

def main():

    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    ex = Ui_Form()
    ex.setupUi(w)
    w.show()
    return app.exec_()


if __name__ == '__main__':
    sys.exit(main())