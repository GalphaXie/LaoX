import socket


def send_msg(upd_socket):
    """发送消息函数"""
    ip = input("请输入目标ip:")
    port = int(input("请输入目标port:"))
    data_str = input("请输入要发送的消息内容：")
    upd_socket.sendto(data_str.encode("utf-8", errors="ignore"), (ip, port))


def recv_msg(udp_socket):
    """接收消息的函数"""
    recv_data, addr = udp_socket.recvfrom(1024)
    print("收到消息:{}".format(recv_data.decode("gbk")))
    print("对方ip和port://{}:{}".format(*addr))


def main(server_ip, server_port):
    # 1.创建upd通信套接字
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定ip和端口
    udp_server.bind((server_ip, server_port))
    # 3.实现功能
    print("-------------简易版udp聊天器-------------------")
    print("提示：【0】退出操作；【1】发送消息；【2】接收消息")
    while True:
        op = input("请输入要进行的操作:")
        if op == '0':
            print("你选择退出聊天器")
            break
        elif op == '1':
            send_msg(udp_server)
        elif op == '2':
            recv_msg(udp_server)
        else:
            print("输入的操作信息有误")

    # 5.关闭套接字
    udp_server.close()
    

if __name__ == "__main__":
    # server_ip = "10.90.93.239"
    server_ip = ""
    server_port = 8080
    main(server_ip, server_port)

####################################################################################
"""
笔记：


"""