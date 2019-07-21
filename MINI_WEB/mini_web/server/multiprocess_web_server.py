#!/usr/bin/python3
# file: multiprocess_web_server.py
# Created by Guang at 19-7-19
# description:

# *-* coding:utf8 *-*
import multiprocessing
import socket
import re


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1.接收浏览器发送过来的请求， 即HTTP请求
    # GET / HTTP/1.1
    request = new_socket.recv(1024).decode('utf-8')
    # print("-" * 100)
    # print(request)
    if not request:
        new_socket.close()
        return
    request_lines = request.splitlines()
    # print(request_lines)

    # GET /index.html HTTP/1.1
    # GET POST DELETE
    file_name = ""
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        print("*" * 50, file_name)
        if file_name == "/":
            file_name = "/index.html"

    # 2.返回HTTP格式的数据
    try:
        print("./html" + file_name)
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

    # 这里必须再关闭一次， 底层文件描述符
    new_socket.close()


def main():
    """主函数: 整体控制"""
    # 1.创建套接字
    listen_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定ip和port
    local_addr = ("", 8888)
    listen_server.bind(local_addr)
    # 3.主动变被动
    listen_server.listen(128)

    while True:
        # 4.等待新客户端的连接
        new_socket, client_addr = listen_server.accept()

        # 5.为这个客户端服务
        p = multiprocessing.Process(target=service_client, args=(new_socket, ))
        p.start()
        # 进程类实现的并发服务器，必须要在这里也new_socket.close一次； 原因：文件描述符 fd
        new_socket.close()

    # 关闭监听套接字
    listen_server.close()


if __name__ == '__main__':
    main()
