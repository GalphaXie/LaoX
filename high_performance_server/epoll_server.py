#!/usr/bin/python3
# file: epoll_server.py
# Created by Guang at 19-7-25
# description:

# *-* coding:utf8 *-*

import socket
import re
import select


def handle_client(request, new_socket):
    """为这个客户端服务"""
    # 1. 接收浏览器发送过来的请求 ，即http请求
    request_lines = request.splitlines()
    if not request_lines:
        return
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print("*"*50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2. 返回http格式的数据，给浏览器

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-----"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body

        new_socket.send(response)


def main():
    """主体控制"""
    # 1.创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.配置服务端主动关闭的时候， 自动释放端口资源
    tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 3.绑定addr
    tcp_socket_server.bind(('', 7788))
    # 4.主动变被动， 并设置队列的长度
    tcp_socket_server.listen(128)
    # 5.设置监听套接字为非阻塞， 一旦这样设置，那么在原来需要accept的位置如果没有顺利的被建立连接解阻塞，将抛出异常，可以供我们try捕获
    tcp_socket_server.setblocking(False)

    # new_sockets = list()  # 列表做消息队列，队列中装 socket引用 ，而不是数据

    # 创建 epoll 对象
    epl = select.epoll()

    # 注册事件到epoll中
    # epoll.register(fd[, eventmask])
    # 注意，如果fd已经注册过，则会发生异常
    # 将创建的套接字添加到epoll的事件监听中
    epl.register(tcp_socket_server.fileno(), select.EPOLLIN)

    # 创建一个字典来保存 fd 和 socket 之间的映射关系
    fd_event_dict = dict()
    while True:

        # 默认会阻塞, 知道os检测到数据到来, 通过事件通知方式告诉这个程序，此时才会解阻塞 [(fd, event), (fd, event)]
        # 一次会获得一个或多个底层有消息驱动的 fd和event 元祖
        fd_event_list = epl.poll()
        # [(fd, event), (套接字对应的文件描述符, 这个文件描述符到底是什么事件 例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            if fd == tcp_socket_server.fileno():
                new_socket, client_addr = tcp_socket_server.accept()
                print('有一个新的客户端连接过来...')
                # 向epoll中注册 新的socket 的可读事件
                epl.register(new_socket.fileno(), select.EPOLLIN)
                # 保存映射关系
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断有客户端发送数据过来, 接收数据
                # 已知: 可以从socket对象中通过 fileno 获取其文件描述符， 但是不能直接通过文件描述符获取 socket 对象
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8', errors='ignore')
                if recv_data:
                    print("接收到客户端发送过来的数据: %s" % recv_data)
                    # 为这个新来的客户端服务
                    handle_client(recv_data, fd_event_dict[fd])
                else:
                    # 对方调用了close导致了没有报出阻塞异常，但是数据为空
                    print("当前客户端关闭连接....")
                    fd_event_dict[fd].close()
                    epl.unregister(fd)  # 注销
                    del fd_event_dict[fd]

    # 8.关闭监听套接字
    tcp_socket_server.close()


if __name__ == '__main__':
    main()

"""
笔记：
1.epoll服务器高效率在于主要实现了两个重要功能:
- 1.将socket套接字的文件描述符放在 应用程序和操作系统 共用的存储区域实现通信， 省去了从应用程序空间拷贝到操作系统空间的过程；
- 2.使用 事件通知 代替 轮询操作；

"""
