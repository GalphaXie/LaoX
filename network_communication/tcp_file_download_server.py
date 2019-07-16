# *-* coding:utf8 *-*

import socket


def get_file_content(file_name):
    """获取文件的内容"""
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as e:
        print("打开文件异常")
    else:
        return file_content


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
    recv_data= new_socket.recv(1024).decode("utf-8")
    # 6.判断下载的文件是否存在， 如果存在： 读取文件内容并返回
    if recv_data:
        print("收到客户端希望下载的文件名：", recv_data)
        # 获取文件内容
        file_content = get_file_content(recv_data)
        if file_content:
            # 6.响应客户端
            new_socket.send(file_content)
            print("发送文件内容结束...")
        print("文件内容为空")
    # 7.关闭套接字(子服务器端)
    new_socket.close()
    # 8.关闭套接字(总监听客户端)
    tcp_server.close()


if __name__ == '__main__':
    ip = ''
    port = 8083
    main(ip, port)


####################################################################################
"""
笔记：
1. recv(1024).decode()  链式调用: 相当于 recv(1024)方法的返回值继续调用decode() 方法
2. 打开文件的两种方式比较：
- with 的优势是， 一定可以关闭 ，但是是否可以正常打开不确定， 所以常用在 以写的方式打开文件中；
- open 的优势是， 当是文件打开异常的时候， 通过报错， 而不再需要去关闭文件， 常用在 以读的方式打开文件， 结合try...except使用
"""