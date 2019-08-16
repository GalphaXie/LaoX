#!/usr/bin/python3
# file: __init__.py.py
# Created by Guang at 19-8-15
# description:

# *-* coding:utf8 *-*


class ModelMetaClass(type):
    def __new__(cls, cls_name: str, parent_cls: tuple, attrs: dict):
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断v是否是元组而不是k，下面调用的时候传递的是元组；Djoingo框架不是元组而是类，
            # 所以，判断方式是否有变，而这个又和  多继承有否关系
            if isinstance(v, tuple):
                print("find mappings:%s--->%s" % (k, v))
                mappings[k] = v

        # 删除原来字典已经存在的属性
        for k in mappings.keys():
            attrs.pop(k)

        attrs["__mappings__"] = mappings
        attrs["__table__"] = cls_name

        return type.__new__(cls, cls_name, parent_cls, attrs)


class Model(object, metaclass=ModelMetaClass):

    def __init__(self, **kwargs):

        for k, v in kwargs.items():
            # self.k = v  # 不能满足要求, 我们需要的是 k是动态变化的, 这里显然不对
            setattr(self, k, v)

    def save(self):
        fields = list()
        args = list()
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            # 这个重要
            args.append(getattr(self, k, None))
        # 1.获取表名  self.__table__ 通过实例对象self来获取 类属性 __table__
        # 2.获取要插入的字段
        temp_args = list()
        for arg in args:
            if isinstance(arg, int):
                temp_args.append(str(arg))
            elif isinstance(arg, str):
                temp_args.append("""'{}'""".format(arg))

        sql = "insert into %s (%s) values (%s)" % (self.__table__, ",".join(fields), ",".join(temp_args))

        print('SQL: %s' % sql)


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


if __name__ == '__main__':
    instance = User(uid=123, name="xiaowang", email="xxxx@163.com", password="123456")
    instance.save()
    # 对应如下sql语句
    # insert into User (username,email,password,uid)
    # values ('Michael','test@orm.org','my-pwd',12345)
