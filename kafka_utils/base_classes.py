# -*- coding: utf-8 -*-
"""
1.kafka 主要有两个部分: producer & consumer ,  定义两个相关的类
2.还涉及到 日志部分 命令解析部分(脚本传参) 等辅助模块
3.



"""

import logging
import time
import os

import sys

from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable, InvalidCommitOffsetSizeError

from .conf import BOOTSTRAP_SERVERS

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 1.实例化一个日志管理器， 并设置name和日志等级
logger = logging.getLogger("kafka_consumer").setLevel(logging.INFO)

# 2.新建一个文本处理器讲日志写入磁盘文件， 需要配置：  文本路径， 日志格式化器，
logfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'kafka_consumer.log')
fh = logging.FileHandler(logfile, mode="a").setLevel(logging.INFO)  # 文本处理器
# 格式化器
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# 格式化器加入 文件处理器
fh.setFormatter(formatter)

# 3.添加日志文本处理器到 日志管理器中
logger.addHandler(fh)


class MyKafkaConsumer(object):
    """
    kafka消费者类
    1.实例化一个kafka——client， 解决 连接的稳定性和重连问题
    2.主要的监听程序；
    3.监听不同topic后的对应处理程序

    6.需要配置topic监听列表， topics=[topic_1, topic_2]

    5.需要配置监听的主题：主题对应的处理函数
    topic_dict = {topic_1: topic_1_func, topic_2: topic_2_func}

    """

    def __int__(self, topic_dict: dict):
        self.consumer = self.init_consumer()
        self.topic_dict = topic_dict

    def init_consumer(self):
        """链接kafka服务器, 创建consumer, 订阅topic"""

        tryTimes = 0
        maxTimes = 10
        elaspeTime = 30
        consumer = None

        while True:
            try:
                consumer = KafkaConsumer(bootstrap_servers=[BOOTSTRAP_SERVERS], enable_auto_commit=False,
                                         auto_offset_reset='latest', group_id="success")
            except NoBrokersAvailable:
                logger.error("kafka服务器异常")
            except Exception as e:
                logger.error("其他未知异常： %s" % e)
            else:
                logger.info("kafka成功连接服务器")
                break

            tryTimes += 1
            if tryTimes > maxTimes:
                logger.info("kafka无法连接服务器,超过次数{}/{}".format(tryTimes, maxTimes))
                break

            time.sleep(elaspeTime)

        return consumer

    def run(self, topics: list):
        """巡检任务下发接收主程序"""
        consumer = self.consumer
        if consumer:
            consumer.subscribe(topics=topics)  # 订阅消费主题, 可以同时订阅多个topics=['topic_1', 'topic_2']

            while True:
                consumer.poll(1)
                for message in consumer:
                    print("%s:%d:%d: key=%s value=%s" % (
                        message.topic, message.partition, message.offset, message.key, message.value))

                    func = self.topic_dict.get(message.topic, None)
                    if func:
                        try:
                            print("执行： %s" % func)
                        except Exception as e:
                            logger.error("执行： %s 出现异常: %s" % (func, e))
                            try:
                                consumer.commit_async()  # 异步提交
                            except InvalidCommitOffsetSizeError:
                                logger.error("kafka提交偏移量异常")


if __name__ == '__main__':
    my_kafka_consumer = MyKafkaConsumer()
    my_kafka_consumer.run(topics=['topic_1', 'topic_2'])
