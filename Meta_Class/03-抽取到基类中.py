class Modelmetaclass(type):
    def __new__(cls, class_name, bases, class_attrs):
        mappings = dict()
        # 判断是否需要保存
        for k, v in class_attrs.items():
            if isinstance(v, tuple):  # 判断v是否是元组而不是k，下面调用的时候传递的是元组；Djoingo框架不是元组而是类，
                # 所以，判断方式是否有变，而这个又和  多继承有否关系
                print("find mappings:%s--->%s" % (k, v))
                mappings[k] = v

        # 删除原来字典已经存在的属性
        for k in mappings.keys():  # 这里的处理，将遍历操作和删除操作分开，避免出现问题，点赞
            class_attrs.pop(k)

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        class_attrs["__mappings__"] = mappings  # 保存属性和列的映射关系
        class_attrs["__table__"] = class_name  # 假设表名和类名一致

        return type.__new__(cls, class_name, bases, class_attrs)


class Model(object, metaclass=Modelmetaclass):
    def __init__(self, **kwargs):  # 为何需要定义__init__方法？
        for name, value in kwargs.items():  # 这里为何用kwargs，上面为何用 **kwargs
            setattr(self, name, value)  # name-->各个属性名，value-->各个属性名要指向的内容

    def save(self):  # 因为save没有接受参数，而又要传参数，所以要加上__inti__方法
        fields = list()
        args = list()
        for k, v in self.__mappings__.items():
            fields.append(v[0])  # 取出元组中对应的字段名，以备后面sql语句使用
            args.append(getattr(self, k, None))  # 这三个参数的含义...

        args_temp = list()
        for temp in args:
            # 判断如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        # 要完成下列的语句，对应需求来挨个找出解决方案
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)

        


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")



u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
# print(u.__dict__)
u.save()
