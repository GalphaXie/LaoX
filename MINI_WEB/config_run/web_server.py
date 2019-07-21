import socket
import re
import multiprocessing
import sys
# import dynamic.mini_frame


class WSGIServer(object):
    def __init__(self, ip, port, application, static_path):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind((ip, port))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

        self.application = application

        self.static_path = static_path

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1. 接收浏览器发送过来的请求 ，即http请求  
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode("utf-8")
        # print(">>>"*50)
        # print(request)

        request_lines = request.splitlines()
        print(request_lines[0])

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
        # 2.1 如果请求的资源不是以.py结尾，那么就认为是静态资源（html/css/js/png，jpg等）
        if not file_name.endswith(".py"):
            try:
                f = open(self.static_path + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_socket.send(response.encode("utf-8"))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                # 2.2 准备发送给浏览器的数据---boy
                # response += "hahahhah"

                # 将response header发送给浏览器
                new_socket.send(response.encode("utf-8"))
                # 将response ic.mini_frame.applicationbody发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源的请求

            env = dict()  # 这个字典中存放的是web服务器要传递给 web框架的数据信息
            env['PATH_INFO'] = file_name
            # {"PATH_INFO": "/index.py"}

            # body = dynamic.mini_frame.application(env, self.set_response_header)
            body = self.application(env, self.set_response_header)

            header = "HTTP/1.1 %s\r\n" % self.status

            for temp in self.headers:
                header += "%s:%s\r\n" % (temp[0], temp[1])

            header += "\r\n"

            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode("utf-8"))

        # 关闭套接
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("server", "mini_web v8.8")]
        self.headers += headers

    def run_forever(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    print(sys.argv)  # 显然是个列表， 中间的元素是字符串
    if len(sys.argv) == 3:
        try:
            addr = sys.argv[1].split(":")
            ip = addr[0] if len(addr) == 2 else ""
            port = int(addr[1]) if len(addr) == 2 else int(addr[0])
            # frame_name:app_name
            ret = re.match(r"([^:]+):(.*)", sys.argv[2])
            if ret:
                frame_name_str = ret.group(1)
                app_name_str = ret.group(2)
            else:
                raise Exception("传参错误")
        except Exception as e:
            print("请按照：python3 web_server.py [ip:][port] frame_name:application_name 调用服务器")
        else:

            # 读取配置文件
            with open("web_config.conf") as f:
                conf = f.read()
            conf_dict = eval(conf)

            # 导入模块
            # import frame_name  # 自动去导入 frame_name.py 模块
            sys.path.append(conf_dict["DYNAMIC_PATH"])
            frame_name = __import__(frame_name_str)
            app_name = getattr(frame_name, app_name_str)

            wsgi_server = WSGIServer(ip, port, app_name, conf_dict["STATIC_PATH"])
            wsgi_server.run_forever()
    else:
        print("请按照：python3 web_server.py [ip:][port] frame_name:application_name 调用服务器")


if __name__ == "__main__":
    main()
