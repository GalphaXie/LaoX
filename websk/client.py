from socketIO_client import SocketIO, BaseNamespace

SOCKET_HOST = "10.90.93.239"

SOCKET_PORT = 3000

msg = "ping"


def msg_deal(*args):
    print(*args)
    # print(**kwargs)


socket_client = SocketIO(host=SOCKET_HOST, port=SOCKET_PORT)

socket_client.emit(None, data={"data": "ping"})
socket_client.on("heart ping", callback=msg_deal)

socket_client.wait(seconds=100)

