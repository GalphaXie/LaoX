#!/usr/bin/python3
# file: server.py
# Created by Guang at 19-7-23
# description:

# *-* coding:utf8 *-*

import asyncio
import websockets


async def echo(websocket, path):
    async for message in websocket:
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, 'localhost', 8765))
asyncio.get_event_loop().run_forever()