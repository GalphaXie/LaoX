import json

import requests
import uuid

from json.decoder import JSONDecodeError

unique_id = uuid.uuid4()


def apply_accounts():
    """账号申请"""
    # 1.申请账号 URL
    url = "https://aloha.sf.ucloud.cn/gw/hp/mission/create"

    data = {
        "name": str(unique_id),  # 项目名称, 必须唯一, 如果冲突会报错
        "type": "face",  # 资源绑定数据类型
        "days": 3,  # 资源持续天数
        "count": 5  # 创建资源数量
    }

    print(data)

    resp = requests.post(url=url, json=data)

    resp.raise_for_status()

    ret = resp.json()

    print(ret)


def login_redirect():
    """登录跳转"""

    token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"

    # 2.数交登录跳转 URL
    url = "https://aloha.sf.ucloud.cn/gw/account/callback?token=" + token
    # url = "http://192.168.190.145:8001/account/callback?token=" + token
    # url = "http://127.0.0.1:8001/gw/account/callback?token=" + token     # http://127.0.0.1:8001/account/callback

    resp = requests.get(url=url)

    resp.raise_for_status()

    ret = resp.content.decode()

    print(ret)

    # json.loads(ret)


def get_account():
    """回传token, 获取账号信息"""
    url = "http://data.sh.gov.cn/zq/api/sandbox_name/"

    headers = {"Authorization": "Token ",  # token值验证
               "Content-Type": "application/json"  # 请求类型
               }


    print("-" * 50)
    try:
        resp = requests.post(url=url, headers=headers)
    except requests.exceptions.ConnectionError as e:
        print(e)
    print("-" * 50)


    try:
        resp.raise_for_status()
    except Exception as e:
        print(e)
        try:
            json.loads(resp.content)
        except JSONDecodeError:
            print("JSONDecodeError")
    else:
        print(resp)



# apply_accounts()
login_redirect()
# get_account()


