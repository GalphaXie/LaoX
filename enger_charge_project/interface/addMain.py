from addgy import Ui_Form
from SucceAdd import Ui_Dialog
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog, QWidget

import sys

# class parentWindow(QWidget):
#     def __int__(self):
#         QWidget.__init__(self)
#         self.main_ui = Ui_Form()
#         self.mian_ui.setupUi(self)

class parentWindow(QWidget,Ui_Form):
    def __init__(self):
        super(parentWindow,self).__init__()
        self.setupUi(self)

class childWindow(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_Dialog()
        self.child.setupUi(self)

if __name__=='__main__':

    app=QApplication(sys.argv)
    window=parentWindow()
    child=childWindow()

    btn = window.pushButton_2
    btn.clicked.connect(child.show)

    window.show()
    sys.exit(app.exec_())



