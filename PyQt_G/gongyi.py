# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gongyi.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 10, 321, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(widget)
        self.pushButton.clicked.connect(widget.read)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "设备的标准工艺"))
        self.pushButton.setText(_translate("widget", "读取文件"))

class MyWindow(QtWidgets.QWidget,Ui_Form):
   def __init__(self):
       super(MyWindow,self).__init__()
       self.setupUi(self)
   def read(self):
       file_name,ok=QFileDialog.getOpenFileName(self,'读取','/home')
       if ok :
          _f=open(file_name,'r')
          with _f:
             data=_f.read()
             self.textBrowser.append(data)
          self.textBrowser.append("读取成功...")
