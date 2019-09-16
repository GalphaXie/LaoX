# 对数据库进行测试添加和删除
import unittest
from demo3_bookDemo import app, db, Author


class DataBaseTestCase(unittest.TestCase):
    # 因为是测试数据的添加和删除，所以需要单独为测试创建一个database
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/booktest_unitest"
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        db.create_all()

    def tearDown(self):
        """在测试完毕之后会进行调用，可以做数据的清除操作"""
        db.session.remove()
        db.drop_all()

    def test_add_and_delete_author(self):
        author = Author(name='哈哈')
        db.session.add(author)
        db.session.commit()

        # 查询
        author = Author.query.filter(Author.name == "哈哈").first()
        self.assertIsNotNone(author)

        # import time
        # time.sleep(15)

        # 删除
        db.session.delete(author)
        db.session.commit()

    def test_query_author(self):
        print("哈哈")


if __name__ == '__main__':
    unittest.main()
