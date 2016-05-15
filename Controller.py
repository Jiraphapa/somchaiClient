import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from views import login, instruction, home, chatOpt, chatRoom, FullTodo, reserveShow, reserveForm, assignment, profile
import json
from Connector import Connector
import sys
#placeholder for user data
globalUserData=None
connector=Connector()
# login page
class Form1(QtWidgets.QWidget, login.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.login.clicked.connect(self.doLogin)
        self.window2 = None
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.pass_entry.returnPressed.connect(self.doLogin)

    def doLogin(self):

        username = self.user_entry.text()
        psw = self.pass_entry.text()
        # authenticate
        data = {'username': username, 'password': psw}
        url = "Somchai/login"

        # post and return user
        result, cookies = connector.postWithData(url, data)

        if not self.isDict(result.text):  # check if result.text can change back to dict, if not then its not a json
            self.dialog(result.text)
        else:
            userData = json.loads(result.text)
            globalUserData=userData
            # setup home
            if self.window2 is None:
                self.window2 = Form2(userData, cookies)
                self.window2.show()
                self.close()
            else:
                print("....")

    # create dialog box
    def dialog(self, mes):
        # initial dialog box
        w = QtWidgets.QDialog(self)
        layout = QtWidgets.QVBoxLayout()

        # massage and button
        massage = QtWidgets.QLabel("Caution : " + mes)
        bt = QtWidgets.QPushButton("OK")

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

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            print("in")
            self.login.clicked()


# home page
class Form2(QtWidgets.QWidget, home.Ui_Form):
    def __init__(self, user, cookie, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
        self.user = user
        self.cookie = cookie
        print("con " + str(self.cookie))
        self.queryTodo()

    def doProfile(self):
        if self.profileWindow is None:
            self.profileWindow = profileForm(self.cookie)
        self.profileWindow.show()

    def doReserveShow(self):
        if self.reserveShow is None:
            self.reserveShow = ReserveShow(self.cookie)
        self.reserveShow.show()

    def doHelp(self):
        if self.helpWindow is None:
            self.helpWindow = Form3()
        self.helpWindow.show()

    def doChat(self):
         if self.chatopWindow is None:
             self.chatopWindow = ChatOptionForm(self.cookie)
         self.chatopWindow.show()

    def doTodo(self,event):
        print("before todo " + str(self.cookie))
        if self.todoWindow is None:
             self.todoWindow = FullTodoForm(self.cookie)
        self.todoWindow.show()

    def closeEvent(self, *args, **kwargs):

        r, self.cookie = connector.post("Somchai/logout", cookie=self.cookie)
        print(r.text)

    def isDict(self, mes):
        try:
            dic = json.loads(mes)
        except ValueError as e:
            return False
        return True


    def queryTodo(self):
        count=6
        #query todoList for that user
        r,cookie=connector.get("Somchai/Todo/getTodo",cookie=self.cookie)
        if not self.isDict(r.text):  # check if result.text can change back to dict, if not then its not a json
            print("no todo yet")
        else:
            todoData = json.loads(r.text)
            print(todoData)
            for todo in todoData:
                self.list_widget.addItem(todoData[todo])
                count-=1
                if(count<0):
                    break


# help page - finishes
class Form3(QtWidgets.QWidget, instruction.Ui_Form):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        self.setStyleSheet("background-color:#ffd200;")

#chat option
class ChatOptionForm(QtWidgets.QWidget, chatOpt.Ui_Form):
      def __init__(self,cookie, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.cookie=cookie
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.joinButton.clicked.connect(self.invokeChat)
        self.chatRoomWindow=None
      def invokeChat(self):
          self.hide()
          if self.chatRoomWindow is None:
            self.chatRoomWindow=ChatRoomForm(self.cookie)
          self.chatRoomWindow.show()


class ChatRoomForm(QtWidgets.QWidget, chatRoom.Ui_Form):
     def __init__(self, cookie,parent=None):
        self.cookie=cookie
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")


class FullTodoForm(QtWidgets.QWidget,FullTodo.Ui_Form ):
    def __init__(self,cookie, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setupUi(self)
        self.cookie=cookie
        print("todo "+ str(self.cookie))
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#121317;")
        self.addButton.clicked.connect(self.invokeAssign)
        self.assignWindow=None
        self.finishButton.clicked.connect(self.delTodo)
        if(self.tasksList.count()>0):
            self.tasksList.setCurrentRow(0)
        self.queryTodo()
    def invokeAssign(self):
        if self.assignWindow is None:
             self.assignWindow=assignForm(self.cookie)
        self.assignWindow.show()
        self.assignWindow.assignButton.clicked.connect(self.queryTodo)
    def isDict(self, mes):
        try:
            dic = json.loads(mes)
        except ValueError as e:
            return False
        return True
    def queryTodo(self):
        #query todoList for that user
        r,cookie=connector.get("Somchai/Todo/getTodo",cookie=self.cookie)
        if not self.isDict(r.text):  # check if result.text can change back to dict, if not then its not a json
            print("no todo yet")
        else:
            todoData = json.loads(r.text)
            print(todoData)
            for todo in todoData:
                self.tasksList.addItem(todoData[todo])
    def delTodo(self):
        if(self.tasksList.count()>0):
            detail=self.tasksList.currentItem().text()
            data = {'des':detail}
            url = "Somchai/Todo/deleteTodo"
            listItems=self.tasksList.selectedItems()
            for item in listItems:
                self.tasksList.takeItem(self.tasksList.row(item))
            result, cookies = connector.postWithData(url, data)

class ReserveShow(QtWidgets.QWidget,reserveShow.Ui_Form ):
      def __init__(self, cookie,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.cookie=cookie
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.reserveButton.clicked.connect(self.showForm)
        self.reserveForm=None
        self.setStyleSheet("background-color:#121317;")
        self.showReserved()
      def isDict(self, mes):
        try:
            dic = json.loads(mes)
        except ValueError as e:
            return False
        return True
      def showForm(self):
          if self.reserveForm is None:
             self.reserveForm=ReserveForm(self.cookie)
          self.reserveForm.show()
      def showReserved(self):
        
        r,self.cookie=connector.get("Somchai/getReserved",cookie=self.cookie)
        if not self.isDict(r.text):  # check if result.text can change back to dict, if not then its not a json
            self.dialog(r.text)
        else:
            reserveData = json.loads(r.text)
        print(reserveData)


class ReserveForm(QtWidgets.QWidget,reserveForm.Ui_Form ):
     def __init__(self,cookie, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.cookie=cookie
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#f8e71d;")
     def addReserve(self):
         
         detail=str(self.topicEdit.text())
         start=self.dateTimeEdit.text()
         end=self.dateTimeEdit_2.text()
         room=self.roomList.currentItem().text()
         data={'':detail,}
         url="Somchai/reserve"
        # post and return user
         result, cookies = connector.postWithData(url, data)


class assignForm(QtWidgets.QWidget,assignment.Ui_Form ):
    def __init__(self, cookie,parent=None):
        self.cookie=cookie
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color:#2283f6;")
        self.assignButton.clicked.connect(self.addTask)
        self.fillEmployee()
    def isDict(self, mes):
        try:
            dic = json.loads(mes)
        except ValueError as e:
            return False
        return True
    def fillEmployee(self):
        r,self.cookie=connector.get("Somchai/get_allUser",cookie=self.cookie)
        if not self.isDict(r.text):  # check if result.text can change back to dict, if not then its not a json
            print("no employee yet")
        else:
            emploData = json.loads(r.text)
            print(emploData)
            for employee in emploData:
                self.employeeBox.addItem(emploData[employee])

    def addTask(self):
        usr = str(self.employeeBox.currentText())
        detail=str(self.descripEdit.toPlainText())
        start=self.dateTimeEdit.text()
        end=self.dateTimeEdit_2.text()
        detail=detail+" from "+start+" to "+end
        data = {'user': usr, 'taskDescription':detail,}
        url = "Somchai/Todo/addTodo"
        # post and return user
        result, cookies = connector.postWithData(url, data)



class profileForm(QtWidgets.QWidget,profile.Ui_Form):
     def __init__(self,cookie, parent=None):
        self.cookie=cookie
        QtWidgets.QWidget.__init__(self, parent)
        self.setStyleSheet("background-color:#01cc9f;")
        self.setupUi(self)
        self.setWindowOpacity(0.9)
        print(globalUserData)


if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Form1()
    window.show()
    sys.exit(app.exec_())