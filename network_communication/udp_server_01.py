import socket


def main(server_ip, server_port):
    # 1.创建upd通信套接字
    udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定ip和端口
    udp_server.bind((server_ip, server_port))
    # 3.接收消息
    recv_data, addr = udp_server.recvfrom(1024)
    print("收到消息:{}".format(recv_data.decode("gbk")))
    print("对方ip和port://{}:{}".format(*addr))

    # 4.发送消息
    data_str = input("请输入要发送的消息内容：")
    udp_server.sendto(data_str.encode("utf-8"), addr)

    # 5.关闭套接字
    udp_server.close()


if __name__ == "__main__":
    # server_ip = "10.90.93.239"
    server_ip = ""
    server_port = 8080
    main(server_ip, server_port)

####################################################################################
"""
笔记：

0.udp_socket
- 服务器
    - 创建套接字
    - 绑定本地addr
    - 接收请求|返回响应
    - 关闭套接字
- 客户端
    - 创建套接字
    - 发送请求|接收响应
    - 关闭套接字
    - 补充：客户端也可以绑定端口
注: socket 类似文件操作: 打开， 读写， 关闭

1.socket.socket(Family, type)
- Family : AF_INET
- type: SOCK_DGRAM (UDP)  或  SOCK_STREAM (TCP)

2.bind(addr)
- addr 必须是一个元祖参数
- addr((ip, port))

3.recvfrom(1024) -> tuple : (data, src_addr)
- 1024 大小， 单位是 byte , 可接收数据的最大字节数
- 返回值： 元组： (接收到的数据, (发送方的ip, 发送方的port))
    - recv_data 是一个 bytes 类型的数据， 需要解码
    - addr 也是一个元祖： addr : (ip , port)
- 阻塞状态, 当收到消息才会解阻塞

4.关于编码|解码问题:
- win下：
    - 编码: gbk
    - 解码: utf-8
- Linux下：
    - 编码|解码: utf-8 (统一)
- encode("utf-8", errors="ignore")
    - 可以增加参数 errors="ignore" 或 error="strict"

5.sendto(bytes_data, addr)
- bytes_data: 第一个参数是发送的数据，必须是 bytes 类型的数据；
- addr: 元祖， (ip, port)


"""
##############################################################################
