from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 设置连接数据
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test2'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# 实例化SQLAlchemy对象
db = SQLAlchemy(app)


# 用户及收藏新闻的多对多的关系
# 用户表新闻表

tb_student_course = db.Table('tb_user_collection',
                             db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                             db.Column('news_id', db.Integer, db.ForeignKey('news.id'))
                             )


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.INTEGER, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    courses = db.relationship('News', secondary=tb_student_course,
                              backref=db.backref('users', lazy='dynamic'),
                              lazy='dynamic')


class News(db.Model):
    __tablename__ = "news"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(64), unique=True)



#定义模型类-作者
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    au_book = db.relationship('Book',backref='author')
    def __repr__(self):
        return 'Author:%s' %self.name

#定义模型类-书名
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32))
    author_id = db.Column(db.Integer,db.ForeignKey('author.id'))
    def __str__(self):
        return 'Book:%s,%s'%(self.info,self.lead)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':


    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话

    bk1 = Book(name='老王回忆录')
    bk1.author = au1
    bk2 = Book(name='我读书少，你别骗我')
    bk2.author = au2
    bk3 = Book(name='如何才能让自己更骚')
    bk4 = Book(name='怎样征服美丽少女')
    bk5 = Book(name='如何征服英俊少男')

    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()
    # 提交会话
    db.session.commit()


    app.run(debug=True)
