import os
import MySQLdb
import pandas as pd


class CheckFile(object):

    def __init__(self, imei, name):
        self.imei = imei
        self.name = name
        self.path = "标准工艺库/"
        self.isfile = False

    def search_file(self):      # 检查该设备是否有工艺文件，保存至self.isfile
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            os.mkdir(self.path + self.name + "/")
        else:
            if not os.path.exists(self.path + self.name + "/"):
                os.mkdir(self.path + self.name + "/")
            else:
                if len(os.listdir(self.path + self.name + "/")) != 0:
                    self.isfile = os.listdir(self.path + self.name + "/")

        if self.isfile:
            print("\n", self.name, "的工艺有：", *self.isfile)
        else:
            print("\n", self.name, "的标准工艺库为空，请为其创建标准工艺")

    def create_new_craft(self):
        print("\n****目前暂不支持跨月查询，请尽量将标准工艺周期安排在同一个月。****\n"
              "\n****如果不输入  时:分:秒  的信息，程序将默认为 00:00:00****\n")
        start_time = input("\n请输入" + str(self.name) + "的标准工艺起始时间（格式“2019-06-17 10:01:23”）：")
        end_time = input("\n请输入" + str(self.name) + "的标准工艺终止时间（格式“2019-06-17 10:01:23”）：")
        year = start_time[0:4]
        month = start_time[5:7]
        database = "ld_device_data_" + year + month
        connection_1 = MySQLdb.connect(host='www.xzjn18.com',
                                       user="tempUser",
                                       passwd="tempA13%",
                                       port=8301,
                                       db="data", charset='utf8')
        sql = "select update_date as time, total_yggl, total_ygdn " \
              "from " + database + " " \
              "where device_imei = '" + str(self.imei) + "' and update_date between '" + start_time + "' and '" + end_time + "' " \
              "and a_dy != 0 " \
              "order by 1"
        print("\n正在获取", str(self.name), "的数据...")
        data = pd.read_sql(sql, con=connection_1)
        start_time = data.time.min()
        print("\n数据获取成功！")
        material = input("\n请输入该工艺的名称：")
        data.to_csv(self.path + self.name + "/" + self.name + '_' + material + '.csv', index=False)
        print("\n", self.name, "的", material, "工艺保存完成！")
        return data, material, start_time

    def get_exist_craft(self, file_name):

        assert self.isfile

        data = pd.read_csv(self.path + self.name + "/" + file_name, parse_dates=[0])
        material = file_name.split('_')[-1][:-4]
        start_time = data.time.min()

        return data, material, start_time


if __name__ == '__main__':
    check_file = CheckFile('00070019', "1号中频炉")
    check_file.search_file()
    if not check_file.isfile:
        data, material, start_time = check_file.create_new_craft()
    else:
        data, material, start_time = check_file.get_exist_craft(check_file.isfile[0])

