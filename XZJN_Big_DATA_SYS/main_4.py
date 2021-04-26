# *-* coding:utf8 *-*

import os
import datetime
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pymysql import Connection

from param import *  # 不推荐

# from param import top, peak


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings("ignore")

print("\n======欢迎使用行知聚能电力大数据系统======\n")

# MOD1 电费结构
print("\n目前默认的尖峰平谷电费结构为：\n"
      "\n尖：    单价：" + str(top), "元/度    时段：", *top_time,
      "\n峰：    单价：" + str(peak), "元/度    时段：", *peak_time,
      "\n平：    单价：" + str(flat), "元/度    时段：", *flat_time,
      "\n谷：    单价：" + str(bot), "元/度    时段：", *bot_time)


ask = input("\n是否更改电费结构？（Y/N）")  # 字符串

if ask == 'Y' or ask == 'y':  # if ask in ["Y", 'y']

    print("\n正在读取当前目录下的《尖峰平谷电费结构.xlsx》文件...")

    if not os.path.isfile("尖峰平谷电费结构.xlsx"):  # 当前路径下是否有该文件
        print("\n未找到当前目录下的《尖峰平谷电费结构.xlsx》文件！")
        print("\n正在创建空的《尖峰平谷电费结构.xlsx》文件...")
        save = pd.DataFrame(columns=['小时段', '区段', '单价'])
        save['小时段'] = range(24)
        save['区段'] = "尖峰平谷"
        save['单价'] = 0.0
        save.to_excel("尖峰平谷电费结构.xlsx", index=False, encoding='utf-8')
        print("\n创建完成！")

        input("\n请在创建好的《尖峰平谷电费结构.xlsx》文件上标注好区段和单价后，按任意键继续")

    data = pd.read_excel("尖峰平谷电费结构.xlsx", index_col=[0])

    top_time = data.loc[data['区段'] == '尖'].index.to_list()
    peak_time = data.loc[data['区段'] == '峰'].index.to_list()
    flat_time = data.loc[data['区段'] == '平'].index.to_list()
    bot_time = data.loc[data['区段'] == '谷'].index.to_list()

    top = data.loc[data['区段'] == '尖']['单价'].dropna().unique()[0]
    peak = data.loc[data['区段'] == '峰']['单价'].dropna().unique()[0]
    flat = data.loc[data['区段'] == '平']['单价'].dropna().unique()[0]
    bot = data.loc[data['区段'] == '谷']['单价'].dropna().unique()[0]

    print("\n电费结构更改完成！\n"
          "\n更新后的尖峰平谷电费结构为：\n"
          "\n尖：    单价：" + str(top), "元/度    时段：", *top_time,
          "\n峰：    单价：" + str(peak), "元/度    时段：", *peak_time,
          "\n平：    单价：" + str(flat), "元/度    时段：", *flat_time,
          "\n谷：    单价：" + str(bot), "元/度    时段：", *bot_time)

    input("\n请按任意键继续\n\n")

while True:

    # MOD2 设备名单输入
    while True:
        device = input("\n请输入需要查询的设备编号：\n\n"
                       "(1) 1号中频炉           (11) 1号还原炉\n"
                       "(2) 2号中频炉           (12) 2号还原炉\n"
                       "(3) 3号中频炉           (13) 3号还原炉\n"
                       "(4) 4号中频炉           (14) 4号还原炉\n"
                       "(6) 6号中频炉           (15) 5号还原炉\n"
                       "(7) 7号中频炉           (16) 6号还原炉\n"
                       "(8) 8号中频炉\n"
                       "(9) 9号中频炉\n"
                       "(10) 10号中频炉\n"
                       "\n注：目前5号中频炉尚未安装数聚盒，因此以上设备列表并未包含该设备。\n")

        if device in name_dic.keys():
            # TODO 增加异常捕获
            d = int(device)
            name = name_dic[device]
            imei = imei_dic[device]
            break
        else:
            print("\n输入错误！输入设备编号即可！\n")


    # MOD3 标准工艺库

    def pull_data(imei, name):
        print("\n****目前暂不支持跨月查询，请尽量将标准工艺周期安排在同一个月。****\n"
              "\n****如果不输入  时:分:秒  的信息，程序将默认为 00:00:00****\n")
        start_time = input("\n请输入" + str(name) + "的标准工艺起始时间（格式“2019-06-17 10:01:23”）：")
        end_time = input("\n请输入" + str(name) + "的标准工艺终止时间（格式“2019-06-17 10:01:23”）：")
        year = start_time[0:4]
        month = start_time[5:7]
        database = "ld_device_data_" + year + month
        connection_1 = Connection(host='www.xzjn18.com',
                                  user="tempUser",
                                  passwd="tempA13%",
                                  port=8301,
                                  db="data", charset='utf8')
        sql = "select update_date as time, total_yggl, total_ygdn " \
              "from " + database + " " \
                                   "where device_imei = '" + str(
            imei) + "' and update_date between '" + start_time + "' and '" + end_time + "' " \
                                                                                        "and a_dy != 0 " \
                                                                                        "order by 1"
        print("\n正在获取", str(name), "的数据...")
        data = pd.read_sql(sql, con=connection_1)
        start = data.time.min()
        print("\n数据获取成功！")
        return data, start


    def create_new_craft(imei, name):
        data, start_time = pull_data(imei, name)
        material = input("\n请输入该工艺的名称：")
        data.to_csv(path + name + "/" + name + '_' + material + '.csv', index=False)
        print("\n", name, "的", material, "工艺保存完成！")
        return data, material, start_time


    path = "标准工艺库/"
    if not os.path.exists(path):
        os.mkdir(path)  # 如果不存在，创建在当前目录下创建path目录
        os.mkdir(path + name + "/")
        print("\n" + name + "的标准工艺库为空！请为其创建标准工艺库！")
        data, material, start_time = create_new_craft(imei, name)
    else:
        if not os.path.exists(path + name + "/"):
            os.mkdir(path + name + "/")
            print("\n" + name + "的标准工艺库为空！请为其创建标准工艺库！")
            data, material, start_time = create_new_craft(imei, name)
        else:
            if len(os.listdir(path + name + "/")) == 0:  # listdir()当前目录下 所有的文件或目录的列表，如果空则其长度等于0
                print("\n" + name + "的标准工艺库为空！请为其创建标准工艺库！")
                data, material, start_time = create_new_craft(imei, name)
            else:
                # 标准工艺库/2号中频炉/a,b,c
                files = os.listdir(path + name + "/")  # TODO listdir() 查用法
                print("\n" + name + "的标准工艺有：\n")
                for i, file in enumerate(files):  # TODO enumerate() 函数的用法
                    # 【a, b, c】 => 0，a； 1，b; 2,c
                    print(str(i + 1) + '. ' + file[:-4])  # 1.a, 2.b, 3.c
                while True:
                    try:
                        ask = input("\n请选择需要查询的工艺编号，输入0创建新的标准工艺：")
                    except Exception as e:
                        print("请输入正确的工艺编号")
                    if int(ask) - 1 in range(len(files)):
                        data = pd.read_csv(path + name + '/' + files[int(ask) - 1])
                        material = files[int(ask) - 1].split('_')[-1][:-4]
                        start_time = data.time.min()
                        break
                    elif ask == '0':
                        data, material, start_time = create_new_craft(imei, name)
                        break
                    else:
                        print("\n输入错误！请重新输入")


    # MOD 4 开始计算24小时电费趋势

    def get_ele(df):
        ygdn = [df.total_ygdn.min()] + df.resample("H").max().total_ygdn.to_list()

        start = (df.index.min() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")
        end = df.index.max().strftime("%Y-%m-%d %H")
        idx = pd.date_range(start, end, freq="H")
        ele = pd.DataFrame(index=idx, columns=['ele'], data=ygdn)
        ele = ele.diff().dropna()
        return ele


    def get_price(s):
        global top, peak, flat, bot, top_time, peak_time, flat_time, bot_time
        top_price = (s.loc[s.index.hour.isin(top_time), 'ele'] * top).sum()
        peak_price = (s.loc[s.index.hour.isin(peak_time), 'ele'] * peak).sum()
        flat_price = (s.loc[s.index.hour.isin(flat_time), 'ele'] * flat).sum()
        bot_price = (s.loc[s.index.hour.isin(bot_time), 'ele'] * bot).sum()
        return top_price + peak_price + flat_price + bot_price


    data.time = pd.to_datetime(data.time)
    data.set_index('time', inplace=True)
    s = get_ele(data)
    original_total = get_price(s)
    print("\n\n", name, "的", material, "工艺周期总电费为", str(round(original_total, 2)), "元")
    result = pd.DataFrame(index=np.arange(0, 24.5, 0.5), columns=['price', 'ratio'], data=0)
    result.loc[0, 'price'] = original_total

    delta = datetime.timedelta(hours=0.5)
    d = data.loc[:, ['total_ygdn']]

    for j in range(1, 49):

        d.index -= delta
        ele = get_ele(d)

        if j % 2 == 0:
            total = get_price(ele)
            result.loc[j / 2, 'price'] = total
        else:
            ele_temp = pd.DataFrame(index=pd.date_range(ele.index.min(), ele.index.max() + delta, freq='30T'),
                                    columns=['ele'])
            value = (ele.ele / 2).to_list()
            value = [val for val in value for _ in (0, 1)]
            ele_temp.ele = value
            total = get_price(ele_temp)
            result.loc[j / 2, 'price'] = total

    result.ratio = result.price / original_total - 1

    min_hour = result.price.idxmin()
    min_ratio = result.loc[min_hour, 'ratio']
    min_ratio = format(abs(min_ratio), '.2%')
    min_price = result.loc[min_hour, 'price']
    # min_time = start_time + datetime.timedelta(hours=min_hour)

    if min_hour <= 12:
        print("\n最佳的开工时间应该推迟", min_hour, "个小时\n"
                                         "\n最低电费为", round(min_price, 2), "元\n"
                                                                         "\n电费节省比例为", min_ratio, "\n")
    else:
        min_hour = 24 - min_hour
        print("\n最佳的开工时间应该提早", min_hour, "个小时\n"
                                         "\n最低电费为", round(min_price, 2), "元\n"
                                                                         "\n电费节省比例为", min_ratio, "\n")

    input("\n请按任意键继续查询\n")
