class A(object):
    """"""
    a = 0

    def get_a(self):
        """
        :return:
        """
        return self.a + 1


class B(object):
    """"""
    b = 1

    def get_b(self):
        """
        :return:
        """
        return self.b + 2


if __name__ == '__main__':
    if hasattr(A, "a"):
        func = getattr(A, "get_a")
    # 这里有个需要注意的地方， 获得的属性(方法)调用的时候需要参数
    print(func(A))  # 通过类属性的方式

    print(func(A()))  # 通过对象属性的方式

    setattr(B, 'a', 100)
    setattr(B, 'b', 200)

    print(getattr(B, "a", "null"))
    print(getattr(B, "b", "null"))
    print(getattr(B, "c", "null"))


    delattr(B, 'b')
    # delattr(B, 'b')  # 如果删除的属性不存在， 会报错 AttributeError

    print(getattr(B, "b", "B null"))



