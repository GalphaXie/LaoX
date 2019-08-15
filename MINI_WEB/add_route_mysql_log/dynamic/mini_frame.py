"""
分析：
    随着后期的扩展性， 框架中的业务逻辑应该是可以 由开发者方便扩展的， 比如 application函数内部 的 分支语句不应该过长...
解决方法：
- 1.字典映射
- 2.装饰器

问题:  当路径参数具有一致性但是又有动态的部分的时候, 考虑使用正则这种通配性更好的 方式来处理 装饰器的参数
难点:　此时通过字典取出对应的　装饰函数已经不在管用, 需要考虑更新的方式   保存到URL_FUNC_DICT后的url:'/add/\\d{6}\\.html' ,
        显然通过 file_name = "/add/000007.html"  方式是取不出来 对应的函数的


"""

import re
import urllib.parse
import logging
from pymysql import *

template_root = "./templates"

URL_FUNC_DICT = dict()


def route(url):
    def wrapper(func):
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)

        return call_func

    return wrapper


@route(r"/index.html")
def index(file_name: str, ret: object):
    file_name = file_name.replace(".py", ".html")
    with open(template_root + file_name) as f:
        content = f.read()

    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()
    cs.execute("select * from info;")
    my_stock_info = cs.fetchall()
    cs.close()
    conn.close()
    # print(my_stock_info)
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
            </td>
        </tr>"""
    html = ""
    for stock_info in my_stock_info:
        html += tr_template % (
            stock_info[0],
            stock_info[1],
            stock_info[2],
            stock_info[3],
            stock_info[4],
            stock_info[5],
            stock_info[6],
            stock_info[7],
            stock_info[1]
        )

    content = re.sub(r"\{%content%\}", html, content)

    return content


@route(r"/center.html")
def center(file_name: str, ret: object):
    file_name = file_name.replace(".py", ".html")
    with open(template_root + file_name) as f:
        content = f.read()

    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()
    cs.execute(
        "select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on f.info_id=i.id;")
    my_stock_info = cs.fetchall()
    cs.close()
    conn.close()
    # print(my_stock_info)
    tr_template = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>
                    <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                </td>
                <td>
                    <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                </td>
            </tr>"""

    html = ""
    for stock_info in my_stock_info:
        html += tr_template % (
            stock_info[0],
            stock_info[1],
            stock_info[2],
            stock_info[3],
            stock_info[4],
            stock_info[5],
            stock_info[6],
            stock_info[0],
            stock_info[0]
        )

    content = re.sub(r"\{%content%\}", html, content)
    return content


# 给路由添加正则表达式的原因：在实际开发时，url中往往会带有很多参数，例如/add/000007.html中000007就是参数，
# 如果没有正则的话，那么就需要编写N次@route来进行添加 url对应的函数 到字典中，此时字典中的键值对有N个，浪费空间
# 而采用了正则的话，那么只要编写1次@route就可以完成多个 url例如/add/00007.html /add/000036.html等对应同一个函数，此时字典中的键值对个数会少很多
@route(r'/add/(\d{6})\.html')  # /add/\\d{6}\\.html  添加之后变成这个, 没有解决
def add_focus(file_name, ret):
    stock_code = ret.group(1)
    # 创建数据库连接对象和游标对象
    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()
    # 1.校验: 要添加的股票是否存在于 股票信息数据库中, 防止 恶意股票代码
    sql = """select id from info where code=%s;"""
    cs.execute(sql, [stock_code])
    stock = cs.fetchone()  # 元祖 (1,)
    # (2, '000036', '华联控股', '10.04%', '10.80%', Decimal('11.29'), Decimal('10.26'), datetime.date(2017, 7, 20))
    if not stock:
        cs.close()
        conn.close()
        return "数据库查询错误"
    # 2.校验: 要添加的股票在 我的关注数据库中, 是否存在, 防止 恶意请求
    sql = """select * from focus where info_id=%s;"""
    cs.execute(sql, stock)
    focus_line = cs.fetchone()
    if focus_line:
        cs.close()
        conn.close()
        return "添加的数据已经存在请勿重复添加"

    # 3.没有添加, 那么添加
    sql = """insert into focus (info_id) select id from info where code=%s"""
    cs.execute(sql, [stock_code])
    conn.commit()  # 注意,这里要提交, 而且提交是使用 conn 对象而不是 cs 对象
    cs.close()
    conn.close()
    return "添加(%s)成功" % stock_code


@route(r"/del/(\d{6})\.html")
def del_focus(file_name: str, ret: object):
    stock_code = ret.group(1)
    # 创建数据库连接对象和游标对象
    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()
    # 1.校验: 要删除的股票是否存在于 focus数据表中, 防止 恶意股票代码
    sql = """select * from focus where info_id=(select id from info where code=%s)"""
    cs.execute(sql, [stock_code])
    stock = cs.fetchone()  # 元祖 (1,)
    # (2, '000036', '华联控股', '10.04%', '10.80%', Decimal('11.29'), Decimal('10.26'), datetime.date(2017, 7, 20))
    if not stock:
        cs.close()
        conn.close()
        return "要删除的(%s)不存在" % stock_code

    # 3.如果数据库存在, 则删除
    sql = """delete from focus where info_id=(select id from info where code=%s)"""
    cs.execute(sql, [stock_code])
    conn.commit()  # 注意,这里要提交, 而且提交是使用 conn 对象而不是 cs 对象
    cs.close()
    conn.close()
    return "删除(%s)成功" % stock_code


@route(r'/update/(\d{6})\.html')
def update_show_focus(file_name: str, ret: object):
    stock_code = ret.group(1)

    content = ""
    with open(template_root + "/update.html") as f:
        content = f.read()

    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()

    # 1.校验: 要修改的股票是否存在于 focus数据表中, 防止 恶意股票代码
    sql = """select * from focus where info_id=(select id from info where code=%s)"""
    cs.execute(sql, [stock_code])
    stock_tuple = cs.fetchone()  # (13, '', 1)
    cs.close()
    conn.close()
    if not stock_tuple:
        return "要修改的(%s)股票不存在" % stock_code
    # 2. 要修改的股票存在, 查询出旧的股票备注信息, 并展示
    content = re.sub(r"\{%code%\}", stock_code, content)
    content = re.sub(r"\{%note_info%\}", stock_tuple[1], content)

    return content


@route(r'/update/(\d{6})/(.*?)\.html')
def update_save_focus(file_name: str, ret: object):
    stock_code, note_info = ret.group(1), ret.group(2)
    # url乱码问题
    note_info = urllib.parse.unquote(note_info)

    conn = Connection(host="localhost", port=3306, user="root", password="mysql", database="stock_db", charset="utf8")
    cs = conn.cursor()
    # 1.校验: 要修改的股票是否存在于 focus数据表中, 防止 恶意股票代码
    sql = """select * from focus where info_id=(select id from info where code=%s)"""
    cs.execute(sql, [stock_code])
    stock_tuple = cs.fetchone()  # (13, '', 1)
    if not stock_tuple:
        cs.close()
        conn.close()
        return "修改操作错误..."
    # 2.查询的数据存在
    sql = """update focus set note_info=%s where info_id=(select id from info where code=%s)"""
    cs.execute(sql, [note_info, stock_code])
    conn.commit()
    cs.close()
    conn.close()

    return "修改(%s)股票备注成功" % stock_code


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']

    # 添加日志功能
    logging.basicConfig(level=logging.INFO, filename="./log.txt", filemode="a",
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    logging.info("访问的是: %s" % file_name)

    try:
        # print(URL_FUNC_DICT)
        # print(file_name)
        # return URL_FUNC_DICT[file_name](file_name)
        for url, func in URL_FUNC_DICT.items():  # TODO 显然这里会制约并发
            ret = re.match(url, file_name)
            if ret:
                return func(file_name, ret)
        else:
            logging.warning("请求的url(%s)没有对应的函数" % file_name)
            return "请求的url(%s)没有对应的函数...." % file_name
    except Exception as e:
        # print("异常： %s" % e)
        return 'Hello World! 我爱你中国....'
