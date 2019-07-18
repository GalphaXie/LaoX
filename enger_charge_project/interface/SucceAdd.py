# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SucceAdd.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 90, 101, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "新增成功！"))


if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    # dialog=QtWidgets.QDialog()
    ui=Ui_Dialog()
    ui.setupUi(ui)
    ui.show()
    sys.exit(app.exec_())