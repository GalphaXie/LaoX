import socket
from select import select

from collections import deque


host = "127.0.0.1"
port = 9001
fam = 0


hostInfo = socket.getaddrinfo(host, port, fam, socket.SOCK_STREAM, socket.IPPROTO_TCP, socket.AI_PASSIVE)


print(hostInfo)

print(type(hostInfo))


print(hostInfo[0][0])
print(hostInfo[0][1])
print(hostInfo[0][2])

serversocket = socket.socket(hostInfo[0][0], hostInfo[0][1], hostInfo[0][2])

print(serversocket)

rList, wList, xList = select([serversocket], [], [serversocket], 0.1)

print(rList, wList, xList)


deque().insert(0, 10)

opcode, payload = deque((1, bytearray(b'\x81Y{"topic": "heart ping", "time": 1562928993.2842267, "namespace": "/test", "data": "ping"}')))

print(opcode)
print(payload)

