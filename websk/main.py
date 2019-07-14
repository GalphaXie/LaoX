import json

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import conf


class MyWebSocketServer(WebSocket):
    """websocket服务器"""

    def handleMessage(self):
        """处理消息后返回给客户端"""
        msg = self.data
        print(msg, type(msg))

        # TODO 消息处理函数
        # res = msg_deal(msg)

        self.sendMessage(self.data)

    def handleConnected(self):
        # TODO 这里增加日志功能
        print(self.address, 'connected')

    def handleClose(self):
        # TODO 这里增加日志功能
        print(self.address, 'closed')


def msg_deal(msg):
    # 可以在服务端配置 命名空间

    default_namespace = '/test'

    msg_dict = json.loads(msg)
    namespace = msg_dict.get("namespace", default_namespace)
    topic = msg_dict.get("topic", "test")
    data = msg_dict.get("data", "")

    if topic == "heart ping":
        recall_dict = {
            "namespace": namespace,
            "topic": "heart pong",
            "data": "pong"
        }
        recall_msg = json.dumps(recall_dict)
        return recall_msg
    else:
        return msg


if __name__ == '__main__':

    server = SimpleWebSocketServer(host=conf.host, port=conf.port, websocketclass=MyWebSocketServer, selectInterval=0.1)

    server.serveforever()

