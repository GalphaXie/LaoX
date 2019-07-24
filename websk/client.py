import json
from socketIO_client import SocketIO, BaseNamespace

SOCKET_HOST = "10.90.93.244"

SOCKET_PORT = 3000

data = json.dumps({"name": "boonray"})


def msg_deal(*args):
    print(">>>>", *args)
    # print(**kwargs)


socket_client = SocketIO(host=SOCKET_HOST, port=SOCKET_PORT)


class ChatNamespace(BaseNamespace):
    def on_aaa_response(self, *args):
        print('on_aaa_response', args)


chatNamespace = socket_client.define(ChatNamespace, "/test")

chatNamespace.emit("auto recall callback", data)
chatNamespace.on("heart ping", callback=msg_deal)
socket_client.wait(seconds=1)  # TODO 可以优化seconds




# socket_client.emit(None, data={"data": "ping"})
# socket_client.on("heart ping", callback=msg_deal)
#
# socket_client.wait(seconds=100)

