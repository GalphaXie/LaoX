import sys
import os

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QComboBox,
    QTableWidget,
    QAbstractItemView,
    QTableWidgetItem,
    QHeaderView)
import csv
import pandas as pd
import numpy as np

from enger_charge_project.interface.standard_tech import Ui_Form as Std_Tech_Form


class Handle_CSV(object):

    def __init__(self, table):
        self.table = table

    def read_from_file(self):
        """读取csv文件的内容到QTableWidget对象中"""
        i = 0  # 初始化一个计数器
        with open('energy_charge_info.csv', encoding="gbk") as f:
            reader = csv.reader(f)
            for row in reader:
                for content in row:
                    if content == '时间':
                        break  # 这里虽然用的break，但是和通常的用法不一样
                    new_item = QTableWidgetItem(content)
                    self.table.setItem(i - 1, row.index(content), new_item)  # 列， 行， 内容
                # 增加一个计数
                i += 1

    def write_to_file(self):
        # TODO 明天写
        pass


class StandardTechTnterface():

    pass


class WelocomeInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.title = '欢迎使用行知聚能电力大数据系统！'
        self.left = 10
        self.top = 10
        self.width = 840
        self.height = 680
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 查看按钮
        self.button_watch = QPushButton('查看', self)
        self.button_watch.setToolTip('可以点击查看具体的电费结构')
        self.button_watch.move(200, 100)
        self.button_watch.clicked.connect(self.watch_energy_charge_table)

        # 修改按钮
        self.button_update = QPushButton("修改", self)
        self.button_update.setToolTip("可以点击修改具体的电费结构")
        self.button_update.move(400, 100)
        self.button_update.clicked.connect(self.update_energy_charge_table)

        # 返回按钮
        self.button_back = QPushButton('返回', self)
        # self.label_back = QLabel("返回", self.table_energy_charge)
        self.button_back.move(600, 100)
        self.button_back.clicked.connect(self.go_back_welcome)

        # 欢迎标语
        font = QFont()
        font.setFamily("Algerian")
        font.setPointSize(16)
        self.label_welcome = QLabel("欢迎使用行知聚能电力大数据系统！", self)
        self.label_welcome.move(140, 50)
        self.label_welcome.setFont(font)

        # 电费结构标签
        self.label_energy_charge_structure = QLabel("电费结构", self)
        self.label_energy_charge_structure.move(100, 100)

        # 设备选择标签
        self.label_equipment = QLabel("设备选择", self)
        self.label_equipment.move(100, 150)

        # 下拉文本框
        self.ComboBox_equipment_options = QComboBox(self)
        self.ComboBox_equipment_options.move(200, 150)
        items = ['%d号中频炉' % item for item in range(1, 11)]
        items += ["%d号还原炉" % item for item in range(1, 7)]
        self.ComboBox_equipment_options.addItems(items)
        # 下拉文本框的信号机制
        self.ComboBox_equipment_options.currentIndexChanged[str].connect(self.get_value)

        # 电费价格表 实例化
        self.table_energy_charge = QTableWidget(self)
        self.table_energy_charge.resize(640, 400)
        self.table_energy_charge.move(60, 200)
        self.table_energy_charge.setToolTip("双击进行修改")
        # 设置表头的背景色为灰色
        self.table_energy_charge.horizontalHeader().setStyleSheet('QHeaderView::section{background:grey}')
        self.table_energy_charge.setRowCount(24)  # 23行
        self.table_energy_charge.setColumnCount(3)  # 3列
        # 设置随内容自动调整列宽
        self.table_energy_charge.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_energy_charge.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table_energy_charge.setHorizontalHeaderLabels(['时间', "峰值类型", "电价(元/度)"])  # 创建表头
        self.table_energy_charge.hide()  # 必须，默认隐藏

        # 标准工艺库的界面
        self.std_tech_form = Std_Tech_Form()
        self.std_tech_form.setupUi(self.std_tech_form)



        self.show()

    def watch_energy_charge_table(self):
        """查看电费价格表"""
        # 注意： 读取的时候禁止编辑
        self.table_energy_charge.hide()
        self.table_energy_charge.setEditTriggers(QAbstractItemView.NoEditTriggers)  # TODO 有问题
        # 从文件读取
        handle_csv = Handle_CSV(self.table_energy_charge)
        handle_csv.read_from_file()
        # 展示
        self.table_energy_charge.show()


    def update_energy_charge_table(self):
        # 从文件读取(这一步必须的， 当不进行查看直接修改的时候， 默认要有东西供修改)
        self.table_energy_charge.hide()
        self.table_energy_charge.setEditTriggers(QAbstractItemView.DoubleClicked)  # 双击进入修改状态
        # 从文件读取
        handle_csv = Handle_CSV(self.table_energy_charge)
        handle_csv.read_from_file()
        self.table_energy_charge.show()
        # TODO 反向写入文件，以供下一次读取

        item = self.table_energy_charge.selectedItems()
        try:
            origin_item_content = item[0].text()
        except Exception as e:
            pass
        else:
            row = self.table_energy_charge.currentRow()  # 行号， 从0开始计数
            col = self.table_energy_charge.currentColumn()  # 列号，从0开始计数
            if len(item) == 0:
                pass
            else:
                print(item[0].text())
                print(col)
                print(row)

    def go_back_welcome(self):
        self.table_energy_charge.hide()

    def get_value(self, value):
        """获取下拉列表的内容， 并打印"""
        print(value)
        name = value
        # for k, v in name_dic.items():
        #     if v == value:
        #         print(k, v)
        #         imei = imei_dic.get(k, None)
        #
        # data = check_exist_std_hub(name, imei)

        # TODO 跳转到对应的工艺中
        self.std_tech_form.show()

        self.std_tech_form.pushButton_2.clicked.connect(self.std_tech_form.get_time_data)
        # sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcome_interface = WelocomeInterface()
    sys.exit(app.exec_())


