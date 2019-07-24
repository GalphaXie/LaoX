# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestReadText.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from enger_charge_project.origin.param import *

start_time = None
end_time = None
gy_name = None


class Ui_Form(QtWidgets.QWidget):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(528, 453)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 340, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(120, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 150, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(120, 260, 111, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 60, 101, 41))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 210, 101, 21))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 160, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(230, 210, 194, 22))
        self.dateTimeEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dateTimeEdit.setDate(QtCore.QDate(2019, 1, 1))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(230, 260, 194, 22))
        self.dateTimeEdit_2.setDate(QtCore.QDate(2019, 1, 1))
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 返回按钮, 触发窗口关闭
        self.pushButton.clicked.connect(self.close)

        # 保存按钮，触发保存操作
        self.pushButton_2.clicked.connect(self.save_tech)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "工艺界面"))
        self.pushButton_2.setText(_translate("Form", "保存"))
        self.pushButton.setText(_translate("Form", "返回"))
        self.label_2.setText(_translate("Form", "工艺名称："))
        self.label_4.setText(_translate("Form", "工艺完工时间："))
        self.label.setText(_translate("Form", "新增标准工艺"))
        self.label_3.setText(_translate("Form", "工艺开工时间："))

    def get_time_data(self):
        global start_time
        global end_time
        global gy_name
        start_time = self.dateTimeEdit.text()
        end_time = self.dateTimeEdit_2.text()
        gy_name = self.lineEdit.text() # 工艺名称

        print(start_time)
        print(end_time)
        print(gy_name)
        # TODO 将这些数据进行查找操作

        # self.write_to_csv()  # start_time, end_time, gy_name

    def save_tech(self):
        QMessageBox.about(self, "保存", "保存成功")
        self.write_to_csv()

    def write_to_csv(self):
        # start_time, end_time, gy_name
        """将工艺名称， 开始时间， 结束时间写入csv文件保存"""
        print("write_to_csv...")

        pass


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_form = Ui_Form()
    ui_form.setupUi(ui_form)
    ui_form.show()
    ui_form.pushButton_2.clicked.connect(ui_form.get_time_data)
    sys.exit(app.exec_())