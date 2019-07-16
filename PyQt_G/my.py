# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 80, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 80, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 140, 101, 17))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 180, 113, 27))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(self.label.hide)
        self.pushButton_2.clicked.connect(self.label.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "查看"))
        self.pushButton_2.setText(_translate("Form", "修改"))
        self.label.setText(_translate("Form", "标签"))
        self.label_2.setText(_translate("Form", "请输入姓名"))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # w = QtWidgets.QWidget()
    # w.resize(250, 150)
    # w.move(300, 300)
    # w.show()
    ui_form = Ui_Form()
    ui_form.setupUi(ui_form)
    ui_form.show()


    content = ui_form.lineEdit.text()
    print(content)


    sys.exit(app.exec_())

    #
    # ui_form = Ui_Form()
    # ui_form.setupUi()