import pandas as pd
import datetime
import numpy as np


class get_result(object):

    def __init__(self, data, material, start_time):
        self.data = data
        self.material = material
        self.start_time = start_time
        self.freq = 0.5     # 单位：小时

        ele_struct = pd.read_excel("尖峰平谷电费结构.xlsx", index_col=[0])

        self.top_time = ele_struct.loc[ele_struct['区段'] == '尖'].index.to_list()
        self.peak_time = ele_struct.loc[ele_struct['区段'] == '峰'].index.to_list()
        self.flat_time = ele_struct.loc[ele_struct['区段'] == '平'].index.to_list()
        self.bot_time = ele_struct.loc[ele_struct['区段'] == '谷'].index.to_list()

        self.top = ele_struct.loc[ele_struct['区段'] == '尖']['单价'].dropna().unique()[0]
        self.peak = ele_struct.loc[ele_struct['区段'] == '峰']['单价'].dropna().unique()[0]
        self.flat = ele_struct.loc[ele_struct['区段'] == '平']['单价'].dropna().unique()[0]
        self.bot = ele_struct.loc[ele_struct['区段'] == '谷']['单价'].dropna().unique()[0]

    def get_price(self, data):        # 从1min精度的电能数据得出总电费
        ygdn = [data.total_ygdn.min()] + data.resample("H").max().total_ygdn.to_list()

        start = (data.index.min() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H")
        end = data.index.max().strftime("%Y-%m-%d %H")
        idx = pd.date_range(start, end, freq="H")
        ele = pd.DataFrame(index=idx, columns=['ele'], data=ygdn)
        ele = ele.diff().dropna()

        top_price = (ele.loc[ele.index.hour.isin(self.top_time), 'ele'] * self.top).sum()
        peak_price = (ele.loc[ele.index.hour.isin(self.peak_time), 'ele'] * self.peak).sum()
        flat_price = (ele.loc[ele.index.hour.isin(self.flat_time), 'ele'] * self.flat).sum()
        bot_price = (ele.loc[ele.index.hour.isin(self.bot_time), 'ele'] * self.bot).sum()

        return top_price + peak_price + flat_price + bot_price

    def get_price_trend(self):
        d = self.data.set_index('time', inplace=True)
        original_price = self.get_price(d)

        result = pd.DataFrame(index=np.arange(0, 24, self.freq), columns=['price', 'ratio'], data=0)
        result.loc[0, 'price'] = original_price
        delta = datetime.timedelta(hours=self.freq)

        for idx in result.index[1:]:

            d.index += delta
            total = self.get_price(d)

            result.loc[idx, 'price'] = total
            result.loc[idx, 'ratio'] = total/original_price - 1
        self.result = result

    def get_min_info(self, res):
        min_hour = res.price.idxmin()
        min_ratio = res.loc[min_hour, 'ratio']
        min_ratio = format(abs(min_ratio), '.2%')
        min_price = res.loc[min_hour, 'price']
        min_time = start_time + datetime.timedelta(hours=min_hour)
        return min_hour, min_time, min_price, min_ratio

    def get_top_min(self, count=3):
        min_frame = pd.DataFrame(index=range(1, count+1), columns=['time', 'price', 'ratio'], data=0)

        res = self.result.copy()

        for i in min_frame.index:
            min_hour, min_time, min_price, min_ratio = self.get_min_info(res)
            min_frame.loc[i, 'time'] = min_time
            min_frame.loc[i, 'price'] = min_price
            min_frame.loc[i, 'ratio'] = min_ratio

            drop_idx = res[(res.index >= (min_hour - 1)) & (res.index <= (min_hour + 1))].index
            res.drop(drop_idx, inplace=True)

        return min_frame


if __name__ == '__main__':
    from MOD1_check_file import data, material, start_time

    r = get_result(data, material, start_time)
    r.get_price_trend()
    print(r.get_top_min(3))


