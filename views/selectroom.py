from PyQt5 import QtCore, QtGui, QtWidgets

#Choosing Chat avaliable ipaddress
class select_room(object):
    def setup_ui(self, Form):
        self.form = Form
        self.form.setObjectName("Form")
        self.form.resize(401, 371)
        Form.setMaximumSize(QtCore.QSize(401, 371))
        self.listWidget = QtWidgets.QListWidget(self.form)
        self.listWidget.setStyleSheet("background-color:white;font-size:20px;color:magenta;")
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 381, 271))
        self.listWidget.setObjectName("tableWidget")
        #Get Room from database
        self.headlabel = QtWidgets.QLabel(self.form)
        self.headlabel.setGeometry(QtCore.QRect(10, 10, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(30)
        self.headlabel.setFont(font)
        self.headlabel.setStyleSheet("color:pink;")
        self.headlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.headlabel.setObjectName("headlabel")
        self.chat_button = QtWidgets.QPushButton(self.form)
        self.chat_button.setGeometry(QtCore.QRect(120, 330, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(30)
        self.chat_button.setFont(font)
        self.chat_button.setObjectName("chat_button")
        self.chat_button.setStyleSheet("color:white;background-color:magenta;")
        self.retranslateUi(self.form)
        QtCore.QMetaObject.connectSlotsByName(self.form)
        self.form.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.headlabel.setText(_translate("Form", "CHAT SELECT"))
        self.chat_button.setText(_translate("Form", "CHAT"))


