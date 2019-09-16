# 0. 导入蓝图类
from flask import Blueprint

# 1. 初始化蓝图对象
cart_blu = Blueprint("cart", __name__, static_folder="static", template_folder='templates',url_prefix='/cart')

from .views import *



