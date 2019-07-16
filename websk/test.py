import asyncio
import logging
import json
import time
import random
from datetime import datetime
from aiowebsocket.converses import AioWebSocket

namespace = '/test'
topic = "heart ping"
content = "ping"


def gen_test_data(namespace, topic, content):
    """生成json格式的测试数据"""
    data = {
        "namespace": namespace,
        "topic": topic,
        "data": content,
        "time": time.time()
    }

    # json处理
    msg = json.dumps(data)

    return msg


async def startup(uri, header):
    async with AioWebSocket(uri, headers=header) as aws:
        converse = aws.manipulator
        # message = gen_test_data(namespace, topic, content)
        while True:
            message = gen_test_data(namespace, topic, content)
            await converse.send(message)
            print('{time}-Client send: {message}'
                  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))

            time.sleep(5)

            mes = await converse.receive()
            print(mes)

            # mes_dict = json.loads(mes.decode("utf-8"))
            # print(mes_dict)
            # topic = mes_dict["test1"]
            print('{time}-Client receive: {rec}'.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
            time.sleep(random.randint(0, 10))


if __name__ == '__main__':
    remote = 'ws://10.90.93.239:3000'
    # remote = 'ws://echo.websocket.org'
    header = [
        # 'GET ws://120.25.247.85:8081/jswapi HTTP/1.1',
        # 'Host: 120.25.247.85:8081',
        # 'Connection: Upgrade',
        # 'Pragma: no-cache',
        # 'Cache-Control: no-cache',
        # 'Upgrade: websocket',
        # # 'Origin: file://',
        # 'Sec-WebSocket-Version: 13'
        # # 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        # 'Sec-WebSocket-Key: hhgVg7ufGwyP3W/7lHlddA==',
        # 'Sec-WebSocket-Extensions: permessage-deflate; client_max_window_bits'
    ]
    try:
        asyncio.get_event_loop().run_until_complete(startup(remote, header))
    except KeyboardInterrupt as exc:
        logging.info('Quit.')
