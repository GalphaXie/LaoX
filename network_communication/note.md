笔记：

1.socket.socket(AddressFamily, SocketKind)  
- AddressFamily: 基本都是AF_INET：ipv4, 几乎没有ip version6 
    - 还有unix通信 : AF_UNIX
- SocketKind: SOCK_STREAM 或 SOCK_DGRAM

