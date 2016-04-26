from PySide import QtCore, QtGui
from views import login, instruction, home, chatOpt, chatRoom, FullTodo, reserveShow, reserveForm, assignment, profile
import json
import requests
import sys


# login page
class Form1(QtGui.QWidget, login.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.button1.clicked.connect(self.handleButton)
        self.login.clicked.connect(self.doLogin)
        self.window2 = None
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;");

    def doLogin(self):


        username = self.user_entry.text()
        psw = self.pass_entry.text()
        # authenticate
        data = {'username': username, 'password': psw}
        url = "http://127.0.0.1:8000/Somchai/login"

        # post and return user
        result = requests.post(url, data)

        if not self.isDict(result.text):  # check if result.text can change back to dict, if not then its not a json
            self.dialog(result.text)
        else:
            userData = json.loads(result.text)
            # setup home
            if self.window2 is None:
                self.window2 = Form2(userData)
                self.window2.show()
                self.close()
            else:
                print("....")

    # create dialog box
    def dialog(self, mes):
        # initial dialog box
        w = QtGui.QDialog(self)
        layout = QtGui.QVBoxLayout()

        # massage and button
        massage = QtGui.QLabel("Caution : " + mes)
        bt = QtGui.QPushButton("OK")

        # add massage to layout
        layout.addWidget(massage)
        layout.addWidget(bt)

        # set layout to widget
        w.setLayout(layout)
        w.show()

    def isDict(self, mes):
        try:
            dic = json.loads(mes)
        except ValueError as e:
            return False
        return True


# home page
class Form2(QtGui.QWidget, home.Ui_Form):
    def __init__(self, user, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.help_button.clicked.connect(self.doHelp)
        self.chat_button.clicked.connect(self.doChat)
        self.todo_button.mousePressEvent=self.doTodo
        self.todo_label.mousePressEvent=self.doTodo
        self.list_widget.mousePressEvent=self.doTodo
        self.reserve_button.clicked.connect(self.doReserveShow)
        self.profile_button.clicked.connect(self.doProfile)
        self.helpWindow=None
        self.chatopWindow=None
        self.todoWindow=None
        self.reserveShow=None
        self.profileWindow=None
    def doProfile(self):
        if self.profileWindow is None:
            self.profileWindow=profileForm()
        self.profileWindow.show()
    def doReserveShow(self):
        if self.reserveShow is None:
            self.reserveShow=ReserveShow()
        self.reserveShow.show()
    def doHelp(self):
        if self.helpWindow is None:
            self.helpWindow=Form3()
        self.helpWindow.show()
    def doChat(self):
         if self.chatopWindow is None:
             self.chatopWindow=ChatOptionForm()
         self.chatopWindow.show()
    def doTodo(self,event):
        if self.todoWindow is None:
             self.todoWindow=FullTodoForm()
        self.todoWindow.show()


# help page
class Form3(QtGui.QWidget, instruction.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        self.setStyleSheet("background-color:#ffd200;")


class ChatOptionForm(QtGui.QWidget, chatOpt.Ui_Form):
      def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.joinButton.clicked.connect(self.invokeChat)
        self.chatRoomWindow=None
      def invokeChat(self):
          self.hide()
          if self.chatRoomWindow is None:
            self.chatRoomWindow=ChatRoomForm()
          self.chatRoomWindow.show()


class ChatRoomForm(QtGui.QWidget, chatRoom.Ui_Form):
     def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")


class FullTodoForm(QtGui.QWidget,FullTodo.Ui_Form ):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.addButton.clicked.connect(self.invokeAssign)
        self.assignWindow=None
    def invokeAssign(self):
        if self.assignWindow is None:
             self.assignWindow=assignForm()
        self.assignWindow.show()


class ReserveShow(QtGui.QWidget,reserveShow.Ui_Form ):
      def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.reserveButton.clicked.connect(self.showForm)
        self.reserveForm=None
        self.setStyleSheet("background-color:#121317;")
      def showForm(self):
          if self.reserveForm is None:
             self.reserveForm=ReserveForm()
          self.reserveForm.show()


class ReserveForm(QtGui.QWidget,reserveForm.Ui_Form ):
     def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#f8e71d;")


class assignForm(QtGui.QWidget,assignment.Ui_Form ):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#2283f6;")


class profileForm(QtGui.QWidget,profile.Ui_Form):
     def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setStyleSheet("background-color:#01cc9f;")
        self.setupUi(self)
        self.setWindowOpacity(0.9)


if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    #window = Form2()
    window.show()
    sys.exit(app.exec_())