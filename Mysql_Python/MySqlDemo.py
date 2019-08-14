#!/usr/bin/python3
# file: MySqlDemo.py
# Created by Guang at 19-8-14
# description:

# *-* coding:utf8 *-*

from pymysql import *


class DB(object):
    def __init__(self, user, password, database, host="localhost", port=3306, charset="utf8"):
        self.conn = Connection(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=charset)
        self.cursor = self.conn.cursor()

    def __del__(self):
        '''
        销毁的时候关闭链接
        :return:
        '''
        self.cursor.close()
        self.conn.close()

    def exe_sql(self, sql):
        '''
        执行查询的sql语句
        打印查询出来的显示结果
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''
        查询所有商品
        :return:
        '''
        sql = "select * from goods;"
        self.exe_sql(sql)

    def show_all_cates(self):
        '''
        查询所有类别
        :return:
        '''
        sql = "select * from goods_cates;"
        self.exe_sql(sql)

    def show_all_brands(self):
        '''
        查询所有品牌
        :return:
        '''
        sql = "select * from goods_brands;"
        self.exe_sql(sql)

    def add_brand(self):
        '''
        添加一个品牌
        :return:
        '''
        brand = input("请输入商品品牌")
        sql = "insert into goods_brands (name) values ('%s')" % brand
        self.cursor.execute(sql)
        self.conn.commit()

    def get_info_byname(self):
        '''
        根据商品名称查询商品的信息
        :return:
        '''
        name = input("请输入要查询商品名称:")
        # TODO sql注入和防止
        sql = "select * from goods where name='%s'" % name
        print("--------->%s<----------" % sql)
        # self.execute_sql(sql)
        self.cursor.execute(sql, [name])
        print(self.cursor.fetchall())

    @staticmethod
    def print_menu():
        print("-----------京东-----------")
        print("1:所有商品")
        print("2:所有商品分类")
        print("3:所有品牌分类")
        print("4:添加一个品牌分类")
        print("5:查询一个商品的详情")
        return input("请输入对应的序号")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                self.show_all_items()
            if num == "2":
                self.show_cates()
            if num == "3":
                self.show_brands()
            if num == "4":
                self.add_brand()
            if num == "5":
                self.get_info_byname()
            else:
                print("请输入对应的序列号")


def main():
    db = DB(host="localhost", port=3306, user="root", password="mysql", database="jing_dong")
    db.run()


if __name__ == "__main__":
    main()
