# *-* coding:utf8 *-*

import socket


def main(*addr):
    # 1.创建套接字: 类比购买手机
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定addr(元祖：ip, port) : 类比插上新买的手机卡
    tcp_server.bind(addr)
    # 3.套接字：主动变被动 : 设置响铃
    tcp_server.listen(128)
    # 4.等待客户端连接 : 类比等待别人打电话过来
    while True:
        print("等待客户端的到来...")
        new_socket, client_addr = tcp_server.accept()
        print("已经有新的客户端到来， 开始服务...")
        # print(client_addr, type(client_addr))
        # 5.接收客户端的数据
        while True:
            print("等待客户端发起请求...")
            recv_data= new_socket.recv(1024)
            print("收到客户端请求数据：", recv_data.decode("gbk"), type(recv_data))
            """
            - 非常重要： recv 解阻塞有两种情况：
            - 1.收到客户端的数据
            - 2.客户端主动断开连接， 那么会解堵塞； 同时收到的数据 为 b''
            """
            if recv_data:
                # 6.响应客户端
                send_data = input("响应给客户端的数据:")
                new_socket.send(send_data.encode("utf-8"))
            else:
                print("当前客户端已经断开连接")
                # 7.关闭套接字(子服务器端)
                new_socket.close()
                break
    # 8.关闭套接字(总监听客户端)
    tcp_server.close()


if __name__ == '__main__':
    ip = ''
    port = 8082
    main(ip, port)


####################################################################################
"""
笔记：
- 非常重要： recv 解阻塞有两种情况：
    - 1.收到客户端的数据
    - 2.客户端主动断开连接， 那么会解堵塞； 同时收到的数据 为 b''

"""