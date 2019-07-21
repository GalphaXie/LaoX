# *-* coding: utf8 *-*
import re
import socket
import multiprocessing


def handle_client(new_socket):
    """为客户端服务"""
    # 1.接收客户端请求
    recv_data = new_socket.recv(1024).decode("utf-8")
    # print(recv_data)
    request_lines = recv_data.splitlines()
    if not request_lines:
        new_socket.close()
        return
    print(request_lines)
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    file_name = ""
    if ret:
        file_name = ret.group(1)
    print(file_name)
    if file_name == "/":
        file_name = "index.html"

    # 2.构造响应response： headers + body
    # 2.1 构造响应头
    header = "HTTP/1.1 200 OK\r\n"
    header += "\r\n"
    # 2.2 构造响应体
    body = "hello world"

    response = header + body

    new_socket.send(response.encode("utf-8"))
    # 子进程不共享主进程的资源， 所以这里需要单独关闭 new_socket
    new_socket.close()


def main(ip, port):
    """主程序"""
    # 1.创建tcp 套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 2.绑定 addr (ip, port)
    addr = (ip, port)
    tcp_server.bind(addr)
    # 3.套接字主动变为被动
    tcp_server.listen(128)
    # 4.等待客户端链接
    while True:
        new_socket, client_addr = tcp_server.accept()
        # 5.让新的套接字为连接的客户端服务
        # handle_client(new_socket)
        p = multiprocessing.Process(target=handle_client, args=(new_socket, ))
        p.start()
        # 6.关闭连接
        new_socket.close()

    # 关闭监听套接字
    tcp_server.close()


if __name__ == '__main__':
    ip = ""   # 表示本地任意一个ip地址
    port = 9999
    main(ip, port)
