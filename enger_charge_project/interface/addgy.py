# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addgy.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(476, 409)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 111, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(190, 110, 191, 31))
        self.textEdit.setObjectName("textEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(190, 220, 194, 31))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(190, 170, 194, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 300, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "新增标准工艺"))
        self.label_2.setText(_translate("Form", "工艺名称："))
        self.label_3.setText(_translate("Form", "工艺开工时间："))
        self.label_4.setText(_translate("Form", "工艺完工时间："))
        self.pushButton.setText(_translate("Form", "返回"))
        self.pushButton_2.setText(_translate("Form", "保存"))




if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())