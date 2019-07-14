# *-* coding:utf8 *-*

import socket


def main(*addr):
    # 1.创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.绑定addr(元祖：ip, port)
    tcp_server.bind(addr)
    # 3.套接字：主动变被动
    tcp_server.listen(128)
    # 4.等待客户端连接
    new_socket, client_addr = tcp_server.accept()
    # print(client_addr, type(client_addr))
    # 5.接收客户端的数据
    recv_data= new_socket.recv(1024)
    print("收到客户端请求数据：", recv_data.decode("gbk"), type(recv_data))
    # 6.响应客户端
    send_data = input("响应给客户端的数据:")
    new_socket.send(send_data.encode("utf-8"))
    # 7.关闭套接字(子服务器端)
    new_socket.close()
    # 8.关闭套接字(总监听客户端)
    tcp_server.close()


if __name__ == '__main__':
    ip = ''
    port = 8081
    main(ip, port)


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

2.bind(addr)
- addr 必须是一个元组参数
- addr((ip, port))
    - 如果ip是空字符串， 那么 表示 本机的ip 

3.listen(int)
- 参数：可以分配多少个新的socket去进行一对第一的服务, 必须是整数;
- 一般不建议超过 128 个

4.accept() -> tuple: (new_socket_server, client_client) 
- 作用： 等待客户端连接
    - 阻塞状态， 当有客户端连接 会 解阻塞
- 返回值是元组， 第一个参数是生成的 用于服务的子socket_server
- 第二个参数是 客户端地址， 也是一个tuple: (ip, port)

5.recv(1024) -> bytes: data
- 1024 大小， 单位是 byte , 可接收数据的最大字节数
- 返回值： bytes 类型的数据， 
    - 需要解码
- 阻塞状态, 当收到消息才会解阻塞

6.send(bytes: send_data)
- 不同于 sendto,  send只需要传递一个参数

7.关于 addr 补充：



"""