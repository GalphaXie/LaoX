from . import cart_blu
from flask import render_template


# 2. 使用蓝图去注册路由url
@cart_blu.route('/list')

def cart_list():
    return render_template('cart.html')
