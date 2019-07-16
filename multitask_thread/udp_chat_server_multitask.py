import socket
import threading


def sen_msg(udp_server):
    """发送消息"""
    ip = input("请输入目标ip:")
    port = int(input("请输入目标port:"))
    while True:
        data_str = input("请输入要发送的消息内容：")
        udp_server.sendto(data_str.encode("utf-8"), (ip, port))


def recv_msg(udp_server):
    while True:
        recv_data, addr = udp_server.recvfrom(1024)
        print("收到消息:{}".format(recv_data.decode("gbk")))
        print("对方ip和port://{}:{}".format(*addr))


def main(server_ip, server_port):
    # 1.创建upd通信套接字
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定ip和port , 注意是个元祖
    udp_server.bind((server_ip, server_port))
    # 3.接收消息
    t1 = threading.Thread(target=recv_msg, args=(udp_server, ))

    # 4.发送消息
    t2 = threading.Thread(target=sen_msg, args=(udp_server, ))

    t1.start()
    t2.start()

    if len(threading.enumerate()) == 1:
        return


if __name__ == "__main__":
    # server_ip = "10.90.93.239"
    server_ip = ""
    server_port = 8080
    main(server_ip, server_port)

####################################################################################
"""
笔记：

"""
##############################################################################
