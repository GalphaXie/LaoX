#!/usr/bin/python3
# file: multiprocess_web_server.py
# Created by Guang at 19-7-19
# description:

# *-* coding:utf8 *-*
import multiprocessing
import socket
import re
import time


class WSGIServer(object):

    def __init__(self, ip, port):
        # 1.创建套接字
        self.listen_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定ip和port
        self.local_addr = (ip, port)
        self.listen_server.bind(self.local_addr)
        # 3.主动变被动
        self.listen_server.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1.接收浏览器发送过来的请求， 即HTTP请求
        # GET / HTTP/1.1
        request = new_socket.recv(1024).decode('utf-8')
        request_lines = request.splitlines()  # 当客户端主动关闭， 会收到空字符串并解阻塞； 这里会生成空列表
        if not request_lines:
            return
        file_name = ""
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*" * 50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        # 2.返回HTTP格式的数据
        # 假设以 .py 结尾的资源是 动态资源
        if not file_name.endswith(".py"):
            try:
                f = open("./html" + file_name, 'rb')
            except Exception as e:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "----------file not found --------"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据 -- header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据 -- body
                # response += “哈哈哈哈”

                # 将response header 发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response body 发送给服务器
                new_socket.send(html_content)
        else:
            # 动态资源加载
            print(file_name)
            if file_name == "/login.py":
                # 2.1 准备发送给浏览器的数据 -- header
                header = "HTTP/1.1 200 OK\r\n"
                header += "\r\n"
                # 2.2 准备发送给浏览器的数据 -- body
                body = "welcome xxx login website ....<br> login: %s" % time.ctime()
            elif file_name == "/logout.py":
                header = "HTTP/1.1 200 OK\r\n"
                header += "\r\n"
                # 2.2 准备发送给浏览器的数据 -- body
                body = "xxx logout website ....<br> logout: %s" % time.ctime()
            else:
                header = "HTTP/1.1 404 NOT FOUND\r\n"
                header += "\r\n"
                body = "----------file not found --------"
            response = header + body
            new_socket.send(response.encode("utf-8"))

        # 这里必须再关闭一次， 底层文件描述符
        new_socket.close()

    def runserver(self):
        while True:
            # 4.等待新客户端的连接
            new_socket, client_addr = self.listen_server.accept()

            # 5.为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket, ))
            p.start()
            # 进程类实现的并发服务器，必须要在这里也new_socket.close一次； 原因：文件描述符 fd
            new_socket.close()

        # 关闭监听套接字
        self.listen_server.close()


if __name__ == '__main__':
    ip = ''
    port = 8888
    wsgi_server = WSGIServer(ip, port)
    wsgi_server.runserver()
