#!/usr/bin/python3
# file: single_process_nonblock_server.py
# Created by Guang at 19-7-24
# description:

# *-* coding:utf8 *-*

import socket
import time
import re


def handle_client(new_socket, request):
    """为这个客户端服务"""
    # 1.接收浏览器发送过来的请求， 即HTTP请求
    # request = new_socket.recv(1024).decode('utf-8')

    request_lines = request.splitlines()  # 当客户端主动关闭， 会收到空字符串并解阻塞； 这里会生成空列表
    if not request_lines:
        return

    file_name = ""
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2.返回HTTP格式的数据
    # 2.1 静态资源和动态资源， 假设以 xxx.py 结尾的是动态资源
    try:
        # print(">" * 50)
        f = open("./html" + file_name, 'rb')
    except Exception as e:
        body = "----------file not found --------"
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        header += "Content-Length: %d\r\n" % len(body)
        header += "\r\n"
        response = header + body
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据 -- header
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Length: %d\r\n" % len(html_content)
        response += "\r\n"
        # 2.2 准备发送给浏览器的数据 -- body
        # 将response header 发送给浏览器
        new_socket.send(response.encode("utf-8"))
        # 将response body 发送给服务器
        new_socket.send(html_content)

        # 关闭套接字
        # new_socket.close()


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
    # 5.设置监听套接字为非阻塞， 一旦这样设置，那么在原来需要阻塞的位置如果没有顺利的解阻塞，将抛出异常，可以供我们捕获
    tcp_socket_server.setblocking(False)
    # 6.分析：要实现可以实时的接收多个客户端的请求,不会因为要长时间的为一个客户端服务，　而单进程单线程的发生阻塞，　可以考虑两件事：
    # 6.1 不间断的接收客户端请求；　不停的为某一个客户端长时间服务；　所以这两者之前必须要独立出来，　且相互之间可以通信。　
    # 6.2 显然， 应该是要求两个不同'worker'之间要通信， 那么显然： 线程， 进程， 协程都可以。 但是， 也可以通过全局变量(消息队列)来通信啊：列表
    new_sockets = list()  # 列表做消息队列，队列中装 socket引用 ，而不是数据
    while True:
        # 测试：
        time.sleep(1)
        # 5.等待客户端连接
        try:
            new_socket, client_addr = tcp_socket_server.accept()
        except Exception as e:
            # print("等待客户端连接异常: %s" % e)
            pass
        else:
            print('有一个新的客户端连接过来...')
            # 将提供服务的客户端也设置为非阻塞
            new_socket.setblocking(False)
            new_sockets.append(new_socket)

        for new_socket in new_sockets:
            # 6.为这个客户端服务
            try:
                recv_data = new_socket.recv(1024).decode('utf-8', errors='ignore')
            except Exception as e:
                pass
                # print("接收客户端发送数据异常: %s" % e)
                # print("这个客户端没有发送过来数据...")
            else:
                if recv_data:
                    print("接收到客户端发送过来的数据: %s" % recv_data)
                    # 2.为客户端服务：返回响应
                    handle_client(new_socket, recv_data)
                else:
                    # 对方调用了close导致了没有报出阻塞异常，但是数据为空
                    print("当前客户端关闭连接....")
                    new_socket.close()
                    new_sockets.remove(new_socket)

    # 8.关闭监听套接字
    tcp_socket_server.close()


if __name__ == '__main__':
    main()


"""
笔记：
1.配置服务端主动关闭的时候， 自动释放端口资源
    tcp_socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
2.设置监听套接字为非阻塞， 一旦这样设置，那么在原来需要阻塞的位置如果没有顺利的解阻塞，将抛出异常，可以供我们捕获
    tcp_socket_server.setblocking(False)
3.通过响应头中的： Content-Length 来实现长连接， 当浏览器在一次tcp连接中， 当确认收到所有的数据后就关闭请求，进行4次挥手。
    header += "Content-Length: %d\r\n" % len(body)
"""