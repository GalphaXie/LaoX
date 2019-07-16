import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget, QToolButton
# from PyQt5 import QtCore, QtGui, QtWidgets
# from main1 import Ui_main1
# from dianfeijiegou import Ui_dfjg
from main1 import Ui_MainWindow
from dianfeijiegou import Ui_Form
# 这里涉及路径问题， 你要用 相对路径导入
# 记住： Pycharm中， 同一个目录下相互导包， 可能前面要加一个小点；
# 但是如果直接通过 python 解释器 xxx.py 这种形式运行， 则不要加点， 否则报错。


class MainWindow(QMainWindow, Ui_MainWindow):

    close_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # self.btn = QToolButton(self)

        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)


    main_window = MainWindow()
    ui_form = Ui_Form()
    ui_form.setupUi(ui_form)


    main_window.pushButton.clicked.connect(ui_form.show)
    main_window.pushButton.clicked.connect(main_window.hide)
    main_window.pushButton.clicked.connect(main_window.close)

    main_window.show()
    sys.exit(app.exec_())




