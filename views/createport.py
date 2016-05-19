from PyQt5 import QtCore, QtGui, QtWidgets
import urllib
import socket

#Can address Privileges to create room here:
class create_server(object):
    def __init__(self):
        self.host = urllib.request.urlopen('http://ip.42.pl/raw').read().decode('utf-8')

    def setup(self,Form):
        self.host = socket.gethostbyname(socket.gethostname())
        self.form = Form
        self.form.setObjectName("Form")
        self.form.resize(173, 173)
        self.accept_button = QtWidgets.QPushButton(self.form)
        self.accept_button.setGeometry(QtCore.QRect(10, 140, 151, 23))
        self.accept_button.setObjectName("accept_button")
        self.input_label = QtWidgets.QLabel(self.form)
        self.input_label.setGeometry(QtCore.QRect(10, 10, 161, 41))
        self.input_label.setWordWrap(True)
        self.input_label.setObjectName("input_label")
        self.input_box = QtWidgets.QLineEdit(self.form)
        self.input_box.setGeometry(QtCore.QRect(20, 50, 131, 20))
        self.input_box.setObjectName("input_box")
        self.input2_label = QtWidgets.QLabel(self.form)
        self.input2_label.setGeometry(QtCore.QRect(40, 80, 91, 20))
        self.input2_label.setObjectName("input2_label")
        self.input2_box = QtWidgets.QLineEdit(self.form)
        self.input2_box.setGeometry(QtCore.QRect(20, 110, 131, 20))
        self.input2_box.setObjectName("input2_box")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # self.accept_button.clicked.connect(self.cre)
        self.form.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.accept_button.setText(_translate("Form", "Accept"))
        self.input_label.setText(_translate("Form", "Input max people in the server (Max 10 - Min 2)"))
        self.input2_label.setText(_translate("Form", "Input room name"))
