#!/usr/bin/python3
# file: port_sniffer.py
# Created by Guang at 19-9-18
# description:

# *-* coding:utf8 *-*

# 绝大多数成功的网络攻击都是以端口扫描开始的，在网络安全和黑客领域，端口扫描是经常用到的技术，可以探测指定主机上是否
# 开放了指定端口，进一步判断主机是否运行了某些重要的网络服务，最终判断是否存在潜在的安全漏洞，从一定意义上将也属于系统运维的范畴

# 端口扫描器程序:模拟端口扫描器的工作原理，并采用多进程技术提高扫描速度
import socket
import sys
import multiprocessing


def ports(ports_serve):
    # 获取常用端口对应的服务名称
    for port in range(2 ** 16 - 1):
        try:
            ports_serve[port] = socket.getservbyport(port)
        except socket.error:
            pass


def ports_scan(host, ports_service):
    ports_open = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 超时时间的不同会影响扫描结果的精确度
        socket.timeout(0.01)
    except socket.error:
        print('socket creation error')
        sys.exit()
    for port in ports_service:

        try:
            # 尝试连接指定端口
            sock.connect((host, port))
            # 记录打开的端口
            print(host, port)
            ports_open.append(port)
            sock.close()
        except socket.error:
            pass
    return ports_open


if __name__ == '__main__':
    m = multiprocessing.Manager()
    ports_service = dict()  # 2**16 -1
    results = dict()
    ports(ports_service)
    # 创建进程池，允许最多8个进程同时运行
    pool = multiprocessing.Pool(processes=8)
    net = '10.90.93.'
    for host_number in map(str, range(107, 108)):
        host = net + host_number
        # 创建一个新进程，同时记录其运行结果
        results[host] = pool.apply_async(ports_scan, (host, ports_service))
        print('starting ' + host + '...')
    # 关闭进程池，close()必须在join()之前调用
    pool.close()
    # 等待进程池中的进程全部执行结束
    pool.join()

    # 打印输出结果
    for host in results:
        print('=' * 30)
        print(host, '.' * 10)
        for port in results[host].get():
            print(port, ':', ports_service[port])

# Python扩展库netaddr提供了大量可以处理网络地址的类和对象，例如netaddr.valid_ipv4(addr)可以判断addr时否为合法IPv4地址
# netaddr.IPNetwork('10.2.1.0/24')和netaddr.IPRange('10.2.1.0','10.2.1.255')都可以用来生成包含介于10.2.1.0到10.2.1.255之间的IP地址的迭代对象。
