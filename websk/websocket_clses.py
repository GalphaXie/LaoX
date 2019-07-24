# -*- coding: utf-8 -*-
import sys
import time
import logging
import os

from socketIO_client import SocketIO, BaseNamespace

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from websk.conf import SOCKET_HOST, SOCKET_PORT

logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
logging.basicConfig()


class BaseSendMsgSocket(object):
    """这是短连接的websocket发送消息的类"""  # TODO 可以继续完善出 长连接的类

    def __init__(self, socket_host="127.0.0.1", socket_port=3000):
        self.instance_socket = SocketIO(socket_host, socket_port)

    def send_msg(self, namespace, topic, data):
        class ChatNamespace(BaseNamespace):
            def on_aaa_response(self, *args):
                print('on_aaa_response', args)

        chatNamespace = self.instance_socket.define(ChatNamespace, namespace)
        chatNamespace.emit(topic, data)
        self.instance_socket.wait(seconds=1)  # TODO 可以优化seconds


class BaseRecvMsgSocket(object):
    _msg_dict = None

    def __init__(self, socket_host="127.0.0.1", socket_port=3000):
        self.instance_socket = SocketIO(socket_host, socket_port)

    def listen(self, namespace, topic):
        class ChatNamespace(BaseNamespace):
            def on_aaa_response(self, *args):
                print('on_aaa_response', args)

        chatnamespace = self.instance_socket.define(ChatNamespace, namespace)

        def on_update_process(*args):
            _msg_dict = [*args][0]

        chatnamespace.on(topic, on_update_process)

        self.instance_socket.wait()

    @classmethod
    def recv_msg(cls):
        while True:
            if cls._msg_dict is not None:
                return BaseRecvMsgSocket._msg_dict
            else:
                time.sleep(0.1)
                continue


if __name__ == '__main__':

    namespace = '/test'
    # namespace = ''
    topic = 'heart ping'
    # topic = ''
    data = {"heart": 'ping'}

    sk = BaseSendMsgSocket(socket_host=SOCKET_HOST, socket_port=SOCKET_PORT)

    sk.send_msg(namespace, topic, data)