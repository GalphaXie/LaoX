#!/usr/bin/python3
# file: manage.py
# Created by Guang at 19-7-17
# description:

# *-* coding:utf8 *-*
import sys

from PyQt5.QtWidgets import QApplication

# 从自己的文件包中导入
from enger_charge_project.welcome import WelocomeInterface
from enger_charge_project.interface.energy_charge_structure import Ui_Form


def enter_welcome_interface():
    """进入欢迎页面"""
    app = QApplication(sys.argv)
    main_window = WelocomeInterface()

    ui_form = Ui_Form()
    ui_form.setupUi(ui_form)

    main_window.button_watch.clicked.connect(ui_form.show)
    main_window.button_watch.clicked.connect(main_window.hide)
    main_window.button_watch.clicked.connect(main_window.close)

    main_window.show()

    sys.exit(app.exec_())





def main():
    # 1.进入欢迎界面
    enter_welcome_interface()








if __name__ == '__main__':
    main()