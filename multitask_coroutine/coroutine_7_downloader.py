#!/usr/bin/python3
# file: coroutine_7_downloader.py
# Created by Guang at 19-7-21
# description:

# *-* coding:utf8 *-*

import gevent
from gevent import monkey
import urllib.request

# 耗时操作
monkey.patch_all()


def my_downloader(url, file_name):
    resp = urllib.request.urlopen(url, )
    content = resp.read()
    with open(file_name, 'wb') as f:
        f.write(content)


def main():
    gevent.joinall([
        gevent.spawn(my_downloader, "https://p0.meituan.net/movie/bb9f75599bfbb2c4cf77ad9abae1b95c1376927.jpg@160w_220h_1e_1c", '1.jpg'),
        gevent.spawn(my_downloader, "https://p0.meituan.net/moviemachine/7b9b0725ab5feae642e1fbba9fbb90fe3702078.jpg@160w_220h_1e_1c", '2.jpg')
    ])


if __name__ == '__main__':
    main()
