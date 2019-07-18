import numpy as np
import pandas as pd
import os
from param import *
import datetime
import warnings
import matplotlib.pyplot as plt
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


ask = input("\n是否更改电费结构？（Y/N）")

if ask == 'Y' or ask == 'y':

    print("\n正在读取当前目录下的《尖峰平谷电费结构.xlsx》文件...")

    if not os.path.isfile("尖峰平谷电费结构.xlsx"):
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
        connection_1 = MySQLdb.connect(host='www.xzjn18.com',
                                       user="tempUser",
                                       passwd="tempA13%",
                                       port=8301,
                                       db="data", charset='utf8')
        sql = "select update_date as time, total_yggl, total_ygdn " \
              "from " + database + " " \
              "where device_imei = '" + str(imei) + "' and update_date between '" + start_time + "' and '" + end_time + "' " \
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
        os.mkdir(path)
        os.mkdir(path + name + "/")
        print("\n", name, "的标准工艺库为空！请为其创建标准工艺库！")
        data, material, start_time = create_new_craft(imei, name)
    else:
        if not os.path.exists(path + name + "/"):
            os.mkdir(path + name + "/")
            print("\n", name, "的标准工艺库为空！请为其创建标准工艺库！")
            data, material, start_time = create_new_craft(imei, name)
        else:
            if len(os.listdir(path + name + "/")) == 0:
                print("\n", name, "的标准工艺库为空！请为其创建标准工艺库！")
                data, material, start_time = create_new_craft(imei, name)
            else:
                files = os.listdir(path + name + "/")
                print("\n", name, "的标准工艺有：\n")
                for i, file in enumerate(files):
                    print(str(i + 1) + '. ' + file[:-4])
                while True:
                    ask = input("\n请选择需要查询的工艺编号，输入0创建新的标准工艺：")
                    if int(ask) - 1 in range(len(files)):
                        data = pd.read_csv(path + name + '/' + files[int(ask) - 1], parse_dates=[0])
                        material = files[int(ask) - 1].split('_')[-1][:-4]
                        start_time = data.time.min()
                        break
                    elif ask == '0':
                        data, material, start_time = create_new_craft(imei, name)
                        break
                    else:
                        print("\n输入错误！请重新输入")

    # MOD 4 开始计算24小时电费趋势


    def get_ele(df):        # 从1min精度的电能数据得出每小时的用电量
        ygdn = [df.total_ygdn.min()] + df.resample("H").max().total_ygdn.to_list()

        start = (df.index.min() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")
        end = df.index.max().strftime("%Y-%m-%d %H")
        idx = pd.date_range(start, end, freq="H")
        ele = pd.DataFrame(index=idx, columns=['ele'], data=ygdn)
        ele = ele.diff().dropna()
        return ele


    def get_price(s):       # 根据每个标准工艺的每小时用电量和尖峰平谷电费结构，计算出工艺总电费
        global top, peak, flat, bot, top_time, peak_time, flat_time, bot_time
        top_price = (s.loc[s.index.hour.isin(top_time), 'ele'] * top).sum()
        peak_price = (s.loc[s.index.hour.isin(peak_time), 'ele'] * peak).sum()
        flat_price = (s.loc[s.index.hour.isin(flat_time), 'ele'] * flat).sum()
        bot_price = (s.loc[s.index.hour.isin(bot_time), 'ele'] * bot).sum()
        return top_price + peak_price + flat_price + bot_price


    data.set_index('time', inplace=True)
    s = get_ele(data)
    original_total = get_price(s)
    print("\n\n", name, "的", material, "工艺周期总电费为", round(original_total, 2), "元，开工时间为", start_time.strftime("%H:%M:%S"))
    result = pd.DataFrame(index=np.arange(0, 24, 0.5), columns=['price', 'ratio'], data=0)
    result.loc[0, 'price'] = original_total

    delta = datetime.timedelta(hours=0.5)
    d = data.loc[:, ['total_ygdn']]

    for j in range(1, result.shape[0]):
        d.index -= delta
        ele = get_ele(d)
        print(ele)
        if j % 2 == 0:
            total = get_price(ele)
            result.loc[j / 2, 'price'] = total
        else:
            ele_temp = pd.DataFrame(index=pd.date_range(ele.index.min(), ele.index.max() + delta, freq='30T'), columns=['ele'])
            value = (ele.ele / 2).to_list()
            value = [val for val in value for _ in (0, 1)]
            ele_temp.ele = value
            total = get_price(ele_temp)
            result.loc[j / 2, 'price'] = total

    result.ratio = result.price / original_total - 1


    def get_min_info(res):
        min_hour = res.price.idxmin()
        min_ratio = res.loc[min_hour, 'ratio']
        min_ratio = format(abs(min_ratio), '.2%')
        min_price = res.loc[min_hour, 'price']
        min_time = start_time + datetime.timedelta(hours=min_hour)
        return min_hour, min_time, min_price, min_ratio


    res = result.copy()

    # 最低电费
    min_hour, min_time, min_price, min_ratio = get_min_info(res)

    # 次低电费
    drop_idx = res[(res.index >= (min_hour - 1)) & (res.index <= (min_hour + 1))].index
    res.drop(drop_idx, inplace=True)
    min_2_hour, min_2_time, min_2_price, min_2_ratio = get_min_info(res)

    # 第三低电费
    drop_2_idx = res[(res.index >= (min_2_hour - 1)) & (res.index <= (min_2_hour + 1))].index
    res.drop(drop_2_idx, inplace=True)
    min_3_hour, min_3_time, min_3_price, min_3_ratio = get_min_info(res)

    print("\n", material, "工艺的最佳开工时间为：\n"
          "\n1. ", min_time.strftime("%H:%M:%S"), "，此时的电费为", round(min_price, 2), "元，电费节省比例为", min_ratio, "\n"
          "\n2. ", min_2_time.strftime("%H:%M:%S"), "，此时的电费为", round(min_2_price, 2), "元，电费节省比例为", min_2_ratio, "\n"
          "\n3. ", min_3_time.strftime("%H:%M:%S"), "，此时的电费为", round(min_3_price, 2), "元，电费节省比例为", min_3_ratio, "\n")

    input("\n请按任意键继续查询\n")


