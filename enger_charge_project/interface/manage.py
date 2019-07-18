# 入口文件
import sys

from PyQt5 import QtWidgets

from zywu.pyqtTest.SucceAdd import Ui_Dialog
from dianfeijiegou import Ui_Form as dian_UiForm
from main1 import mywindow
from TestReadText import Ui_Form as read_UiForm
from TestReadText import start_time, end_time, gy_name
from mFunction import MainWindow
from pymysql import Connection
import pandas as pd




def conenct_database(start_time, end_time, imei, name):
    """连接数据库获取数据"""
    year = start_time[0:4]
    month = start_time[5:7]
    database = "ld_device_data_" + year + month  # 数据表的名称
    connection_1 = Connection(host='www.xzjn18.com',
                              user="tempUser",
                              passwd="tempA13%",
                              port=8301,
                              db="data", charset='utf8')  # 连接数据库

    sql = "select update_date as time, total_yggl, total_ygdn from " \
          + database \
          + "where device_imei = '" \
          + str(imei) \
          + "' and update_date between '" \
          + start_time \
          + "' and '" \
          + end_time \
          + "' and a_dy != 0 order by 1"

    print("\n正在获取", str(name), "的数据...")
    data = pd.read_sql(sql, con=connection_1)  # 读出SQL数据
    start = data.time.min()  # 找到最小时间
    print("\n数据获取成功！")
    return data, start

def create_new_craft(imei, name): # 创建一个新的工艺
    data, start_time = pull_data(imei, name)
    material = input("\n请输入该工艺的名称：") # data数据包括有功功率与有功电能和时间；调用对事pull_data（）这个函数
    data.to_csv(path + name + "/" + name + '_' + material + '.csv', index=False) # 保存工艺，保存为csv文件path = "标准工艺库/"
    print("\n", name, "的", material, "工艺保存完成！")
    return data, material, start_time

# 你说业务逻辑， 我来帮你封装。具体再去实现，我理一下。保存完， 等一下



def get_dianfei(main_window):
    """查看电费结构"""   # 你的很多命名能不能用 English ， 中文tailow了

    ui_form = dian_UiForm()
    ui_form.setupUi(ui_form)

    main_window.pushButton.clicked.connect(ui_form.show)
    main_window.pushButton.clicked.connect(main_window.hide)
    main_window.pushButton.clicked.connect(main_window.close)



def main():
    # 0.查询数据库
    app = QtWidgets.QApplication(sys.argv)
    # dialog=QtWidgets.QDialog()
    # ui = Ui_Dialog()
    # ui.setupUi(ui)
    # ui.show()

    # 在这里把你的步骤用注视写一下， 每个步骤弄一个函数， 然后分别实现功能。

    # 1.第一步：查看电费
    main_window = MainWindow()
    ui_form = dian_UiForm()
    ui_form.setupUi(ui_form)
    # 我没懂这个操作。 。。。。你先继续捋一捋。 把业务逻辑写清楚。伪代码给我。
    main_window.pushButton.clicked.connect(ui_form.show)
    main_window.pushButton.clicked.connect(main_window.hide)
    main_window.pushButton.clicked.connect(main_window.close)
    # get_dianfei(main_window)
    main_window.show()


    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
