import json

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import conf


connect_clients = []


class MyWebSocketServer(WebSocket):
    """websocket服务器"""

    def wrapper(self):
        """通过装饰器实现"""
        def heartbeat(self, func):
            """实现心跳机制"""
            if self.data:
                try:
                    data_dict = json.loads(self.data)
                except Exception as e:
                    print("错误日志：%s" % e)
                else:
                    if data_dict.get("heart", None) == "ping":
                        try:
                            json_str = json.dumps({"heart": "pong"})
                            self.sendMessage(json_str.decode("utf-8"))
                        except Exception as e:
                            print("解析数据错误")
                func()
        return heartbeat

    # @wrapper
    def handleMessage(self):
        """处理消息后返回给客户端"""

        # 这一段是心跳机制的逻辑  # TODO 装饰器实现一下
        if self.data:
            try:
                data_dict = json.loads(self.data)
            except Exception as e:
                print("错误日志：%s" % e)
            else:
                if data_dict.get("heart", None) == "ping":
                    try:
                        json_str = json.dumps({"heart": "pong"})
                        self.sendMessage(json_str)
                    except Exception as e:
                        print("解析数据错误")
                    else:
                        return  # TODO 必须要加

        for client in connect_clients:
            if client == self:
                continue
            msg = self.data
            print(msg, type(msg))
            # res = msg_deal(msg)
            client.sendMessage(self.address[0] + u' - ' + self.data)

    def handleConnected(self):
        print(self.address, 'connected')
        # TODO 这里增加日志功能
        for client in connect_clients:
            client.sendMessage(self.address[0] + u' - connected')
        connect_clients.append(self)

    def handleClose(self):
        # TODO 这里增加日志功能
        connect_clients.remove(self)
        print(self.address, 'closed')
        for client in connect_clients:
            client.sendMessage(self.address[0] + u' - disconnected')

    def heartbeat(self, func):
        """实现心跳机制"""
        if self.data:
            try:
                data_dict = json.loads(self.data)
            except Exception as e:
                # print("错误日志：%s" % e)
                pass
            else:
                if data_dict.get("heart", None) == "ping":
                    try:
                        json_str = json.dumps({"heart": "pong"})
                        self.sendMessage(json_str.decode("utf-8"))
                    except Exception as e:
                        print("解析数据错误")
            func()


# def msg_deal(msg):
#     # 可以在服务端配置 命名空间
#
#     default_namespace = '/test'
#
#     msg_dict = json.loads(msg)
#     namespace = msg_dict.get("namespace", default_namespace)
#     topic = msg_dict.get("topic", "test")
#     data = msg_dict.get("data", "")
#
#     if topic == "heart ping":
#         recall_dict = {
#             "namespace": namespace,
#             "topic": "heart pong",
#             "data": "pong"
#         }
#         recall_msg = json.dumps(recall_dict)
#         return recall_msg
#     else:
#         return msg


if __name__ == '__main__':

    server = SimpleWebSocketServer(host=conf.host, port=conf.port, websocketclass=MyWebSocketServer, selectInterval=0.1)

    server.serveforever()

