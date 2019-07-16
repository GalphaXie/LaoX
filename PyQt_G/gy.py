# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 10, 341, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 201, 231))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.read)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "读取文件"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">wenben</p></body></html>"))

class MyWindow(QtWidgets.QWidget,Ui_Form):
   def __init__(self):
       super(MyWindow,self).__init__()
       self.setupUi(self)
   def read(self):
       file_name,ok=QFileDialog.getOpenFileName(self,'读取','E:/xzjn/zywu/标准工艺库/1号中频炉_a.csv')
       if ok :
          _f=open(file_name,'r')
          with _f:
             data=_f.read()
             self.textBrowser.append(data)
             self.textBrowser.append("读取成功...")
          self.plainTextEdit.toPlainText()

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    myshow=MyWindow()
    myshow.show()
    sys.exit(app.exec_())