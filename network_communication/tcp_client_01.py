# *-* coding:utf8 *-*

import socket


def main():
    # 1.创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.创建连接, 连接tcp服务器
    ip = input("要访问的服务器ip:")
    port = int(input("要访问的服务器port:"))
    tcp_socket.connect((ip, port))
    # 3. 发送数据给tcp服务器
    while True:
        send_data = input("发送请求数据:")
        if send_data == 'exit':
            break
        tcp_socket.send(send_data.encode("utf-8"))
        # 4. 等待服务器的响应
        recv_data = tcp_socket.recv(1024)
        # print("服务器返回的响应: %s" % recv_data.decode("gbk"))
        print("服务器返回的响应: %s" % recv_data.decode("utf-8"))
    # 5.关闭客户端套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()


####################################################################################
"""
笔记：

0.tcp_socket
- 服务器
    - 创建套接字
    - 绑定addr
    - 监听： 主动变被动 listen
    - 等待连接： accept
    - 接收请求|返回响应 : recv|send
    - 关闭套接字(子套接字和监听套接字)
- 客户端
    - 创建套接字
    - 创建连接
    - 发送请求|接收响应 send | recv
    - 关闭套接字
注: socket 类似文件操作: 打开， 读写， 关闭

1.socket.socket(Family, type)
- Family : AF_INET
- type: SOCK_DGRAM (UDP)  或  SOCK_STREAM (TCP)

2.connect(addr)
- addr 必须是一个元组参数 (server_ip, server_port)
- tcp_client 相比 udp_client 多了 connect 这一步

3.send(bytes: send_data)
- 不同于 sendto,  send只需要传递一个参数


"""