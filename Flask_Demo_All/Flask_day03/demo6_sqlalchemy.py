from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库连接地址
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:mysql@127.0.0.1:3306/test_27"
# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 初始化 SQLAlchemy 对象
db = SQLAlchemy(app)


# 角色  1的一方
class Role(db.Model):
    # 指定该模型对应数据库中的表名，如果不指定为类名小写
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # backref 在这行代码的作用是：给前面的 User添加一个属性，名字叫backref的值
    # 以便可以直接通过 user.role 方法到一的一方的数据
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role %d %s' % (self.id, self.name)

# service mysql restart
# service mysql stop
# service mysql start
# 用户  多的一方
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 添加外键记录一的一方的主键id，为了能够直接查询出一的一方的数据
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return 'User %d %s' % (self.id, self.name)





# 需求，查询user所对应的role数据
# select * from role where id = user.role_id

# 需求，查询role所对应的所有user数据
# select * from user where role_id = role.id

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    db.session.add_all([ro1, ro2])
    db.session.commit()

    user1 = User(name='laowang', role_id=ro1.id)
    user2 = User(name='laoli', role_id=ro1.id)
    user3 = User(name='laozhang', role_id=ro2.id)

    db.session.add_all([user1, user2, user3])
    db.session.commit()

    app.run(debug=True)
