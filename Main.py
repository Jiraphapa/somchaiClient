from PySide import QtGui
from views import login
import sys

def main():
    app = QtGui.QApplication(sys.argv)
    w = QtGui.QWidget()
    l = login.Ui_Form()
    l.setupUi(w)
    w.show()
    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())
