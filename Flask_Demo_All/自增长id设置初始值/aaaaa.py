from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import DDL
from sqlalchemy import event

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:mysql@127.0.0.1:3306/test5"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "fdsfdsfs"

db = SQLAlchemy(app)


class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.BigInteger, primary_key=True, autoincrement='auto')
    name = db.Column(db.String(64), unique=True)


event.listen(
    Author.__table__,
    "after_create",
    DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 100000000001;")
)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    db.drop_all()
    db.create_all()

    author = Author(name='1234')
    db.session.add(author)
    db.session.commit()

    author2 = Author(name='324')
    db.session.add(author2)
    db.session.commit()

    author3 = Author(name='234')
    db.session.add(author3)
    db.session.commit()

    app.run(debug=True)
