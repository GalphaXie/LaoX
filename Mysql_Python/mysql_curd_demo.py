# 这个是我做的练习，中间有很多细节需要完善

from pymysql import connect


class JD(object):
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user="root", password="mysql", database="jing_dong",
                            charset="utf8")
        self.cs = self.conn.cursor()

    def __del__(self):
        self.cs.close()
        self.conn.close()

    @staticmethod
    def print_info():
        print("-------京东商城-------")
        print("1：查询所有商品信息")
        print("2：查询所有商品种类")
        print("3：查询所有商品品牌种类信息")
        print("4：添加一个新商品品牌")
        print("5:根据名字查询商品信息")
        print("6:注册操作")
        print("7:登陆操作")
        print("8:下订单操作")
        num = input("请输入操作选项的序号：")
        return num

    def execute_sql(self, sql):
        self.cs.execute(sql)
        for temp in self.cs.fetchall():
            print(temp)

    def show_all_items(self):
        """查询所有商品信息"""
        sql = "select * from goods"
        self.execute_sql(sql)

    def show_all_cates(self):
        """显示所有商品的分类信息"""
        sql = "select name from goods_cates"
        self.execute_sql(sql)

    def show_all_brands(self):
        """显示所有商品的品牌信息"""
        sql = "select name from goods_brands"
        self.execute_sql(sql)

    def add_brand(self):
        """添加新的商品的种类"""
        goods_brand = input("请输入商品的品牌：")
        sql = """insert into goods_brands (name) values ("%s") """ % goods_brand
        self.cs.execute(sql)
        self.conn.commit()

    def get_info_by_name(self):
        """根据商品名字查询商品信息"""
        find_name = input("请输入商品名称:")
        # sql = """select * from goods where name='%s'""" % find_name
        # print("--------->%s<----------" % sql)
        sql = """select * from goods where name=%s"""
        # 构造列表或者元组参数
        # params = [find_name]
        # self.cs.execute(sql, params)
        # 构造元组
        self.cs.execute(sql, (find_name,))  # 一个元素的元组要加逗号
        ret = self.cs.fetchall()
        print(ret)

    def register(self):
        try:
            name = input("请输入您的用户名：")
            address = input("请输入您的地址信息：")
            tel = input("请输入您的电话信息：")
            passwd = input("请输入您的密码:")
            sql = """insert into customers VALUES (DEFAULT, %s, %s, %s, %s)"""
            self.cs.execute(sql, (name, address, tel, passwd))
            self.conn.commit()
        except Exception as ret:
            print("发生了一个未知的错误！")
        else:
            print("****恭喜您：注册成功！****")

    def login(self):
        name = input("请输入您的用户名：")
        passwd = input("请输入您的密码:")
        # 从客户信息表中查询出数据并并进行比对，输出提示信息
        sql = """select name,passwd from customers""" # 这里其实存在一个问题：同名，所有同时取出账号密码,遍历
        self.cs.execute(sql)
        for line in self.cs.fetchall():
            if line[0] == name:
                if line[1] == passwd:
                    return "登陆成功！"
                else:
                    return "密码输入不正确，请核对后重新输入"
        else:
            return "您未注册，请先注册再登陆"

    def place_an_order(self):
        # 客户通过输入商品名称来下单
        self.get_info_by_name()
        print("下单成功")

    def run(self):
        while True:
            num = self.print_info()
            if num == "1":
                # 1.展示所有商品信息
                self.show_all_items()
            elif num == "2":
                # 2.展示所有商品的种类
                self.show_all_cates()
            elif num == "3":
                # 3.展示所有商品品牌的种类
                self.show_all_brands()
            elif num == "4":
                # 添加商品的品牌
                self.add_brand()
            elif num == "5":
                # 根据名字查询商品信息
                self.get_info_by_name()
            elif num == "6":
                # 用户注册，如果用户没有登陆成功，则提示用户注册
                self.register()
            elif num == "7":
                # 用户登陆
                result = self.login()
                print(result)
            elif num == "8":
                # 下订单：这里其实缺乏一个判断，只有是登陆状态才能获取权限，才能下单
                self.place_an_order()
            else:
                print("输入有误，请重新输入")


def main():
    # 创建实例对象
    jd = JD()
    # 调用对象的run方法执行程序
    jd.run()


if __name__ == "__main__":
    main()
