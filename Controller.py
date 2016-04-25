import connector
from PySide import QtCore, QtGui
from views import login, intruction,home,chatOpt,chatRoom,FullTodo,reserveShow,reserveForm
import sys

#login page
class Form1(QtGui.QWidget, login.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.button1.clicked.connect(self.handleButton)
        self.register_2.clicked.connect(self.handleButton)
        self.window2 = None
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;");
    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form2()
        #self.hide()
        self.window2.show()
        self.hide()
        #window=Form2()
        #window.show()
#home page
class Form2(QtGui.QWidget, home.Home):
    def __init__(self, parent=None):
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
        self.helpWindow=None
        self.chatopWindow=None
        self.todoWindow=None
        self.reserveShow=None

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
#help page
class Form3(QtGui.QWidget, intruction.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        self.setStyleSheet("background-color:#ffd200;")
 #dummy need
class ProfileForm(QtGui.QWidget, intruction.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.95)

class ChatOptionForm(QtGui.QWidget, chatOpt.Ui_Form):
      def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#fe3d50;")
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
class ReserveShow(QtGui.QWidget,reserveShow.Ui_Form ):
      def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
class ReserveForm(QtGui.QWidget,reserveForm.Ui_Form ):
     def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    #window = Form2()
    window.show()
    sys.exit(app.exec_())