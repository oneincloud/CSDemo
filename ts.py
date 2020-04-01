import socket

# TCP服务器端
IP ='0.0.0.0'
# 端号
PORT = 5000
# 定义一次从socker缓冲区最多读入512个字节数据
BUFLEN = 512

# 实例化一个socket对象
# 参数 AF_INET 表示该socket网络层使用IP协议
# 参数 SOCK_STREAM 表示该socket传输层使用tcp协议
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# socket绑定地址和端口
tcp_server_socket.bind((IP,PORT))

# 使socket处于监听状态，等待客户端的连接请求
# 参数5表示最多接受多少个等待连接的客户端
tcp_server_socket.listen(5)
print(f"服务器端启动成功，在{PORT}端口等待客户端连接...")

connection,addr = tcp_server_socket.accept()
print("接受一个客户端连接：",addr)

while True:
    # 尝试读取对方发送的消息
    # BUFLEN 指定从接收缓冲里最多读取多少字节
    recved = connection.recv(BUFLEN)

    # 如果返回空bytes，表示对方关闭了连接
    # 退出循环，结束消息接收
    if not recved:
        break

    # 读取的数据是bytes类型，需要解码为字符串
    info = recved.decode('utf-8')
    print(f"收到对方信息：{info}")

    # 给客户端发送信息，类型也必须是bytes编码
    connection.send(f"服务器端收到了信息：{info}".encode('utf-8'))

# 关闭客户端连接
connection.close()
tcp_server_socket.close()
