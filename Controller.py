import connector
from PySide import QtCore, QtGui
from views import login, intruction,home
import sys


class Form1(QtGui.QWidget, login.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        #self.button1.clicked.connect(self.handleButton)
        self.register_2.clicked.connect(self.handleButton)
        self.window2 = None
        #self.setWindowOpacity(0.95)
        self.setStyleSheet("background-color:#121317;");
    def handleButton(self):
        if self.window2 is None:
            self.window2 = Form2()
        #self.hide()
        self.window2.show()
        self.hide()
        #window=Form2()
        #window.show()

class Form2(QtGui.QWidget, home.Home):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.95)
        self.help_button.clicked.connect(self.doHelp)
        self.helpWindow=None
    def doHelp(self):
        if self.helpWindow is None:
            self.helpWindow=Form3()
        self.helpWindow.show()
class Form3(QtGui.QWidget, intruction.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.9)
 #dummy need
class ProfileForm(QtGui.QWidget, intruction.Ui_Form):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.setWindowOpacity(0.95)



if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)
    window = Form1()
    #window = Form2()
    window.show()
    sys.exit(app.exec_())