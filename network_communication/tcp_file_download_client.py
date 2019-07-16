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
    file_name = input("请输入要下载的文件名:")
    if file_name:
        tcp_socket.send(file_name.encode("utf-8"))
        # 4. 等待服务器的响应
        recv_data = tcp_socket.recv(1024 * 1024)
        if recv_data:
            with open(file_name + "_bak", 'wb') as f:
                f.write(recv_data)
            print("下载结束...")
        else:
            print("下载的文件为空")

    # 5.关闭客户端套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()


####################################################################################
"""
笔记：

"""