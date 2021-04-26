import pymysql
import pandas as pd

imei_dic = {'1': '00070019',
            '2': '0007001e',
            '3': '00070023',
            '4': '00070024',
            '6': '00070021',
            '7': '00070022',
            '8': '00070026',
            '9': '00070025',
            '10': '00070027',
            '11': '0007001d',
            '12': '0007001a',
            '13': '00070016',
            '14': '0007001f',
            '15': '00070017',
            '16': '00070031'}

name_dic = {'1': "1号中频炉",
            '2': "2号中频炉",
            '3': "3号中频炉",
            '4': "4号中频炉",
            '6': "6号中频炉",
            '7': "7号中频炉",
            '8': "8号中频炉",
            '9': "9号中频炉",
            '10': "10号中频炉",
            '11': "1号还原炉",
            '12': "2号还原炉",
            '13': "3号还原炉",
            '14': "4号还原炉",
            '15': "5号还原炉",
            '16': "6号还原炉"}

top = 0.8688
peak = 0.7688
flat = 0.6188
bot = 0.4190

top_time = [19, 20, 21]
peak_time = [8, 9, 10, 15, 16, 17, 18]
flat_time = [7, 11, 12, 13, 14, 22]
bot_time = [0, 1, 2, 3, 4, 5, 6, 23]


def get_data(imei, name):
    start_time = input("\n请输入" + str(name) + "的标准工艺起始时间（格式“2019-06-17 10”）：")
    end_time = input("\n请输入" + str(name) + "的标准工艺终止时间（格式“2019-06-17 10”）：")
    year = start_time[0:4]
    database = "ld_device_hour_report_" + year
    connection_1 = pymysql.connect(host='www.xzjn18.com',
                                   user="readTemp",
                                   passwd="duyue1234%",
                                   port=8300,
                                   db="ldalc", charset='utf8')
    sql = "select dat.hour as time, electricity_use as ele " \
          "from " + database + " dat right join ld_device on dat.device_code=ld_device.device_code " \
          "where device_imei = '" + str(imei) + "' and dat.hour >= '" + start_time + "' and dat.hour <= '" + end_time + "' " \
          "order by 1"
    print("\n正在获取", str(name), "的数据...")
    data = pd.read_sql(sql, con=connection_1)
    return data



