# === TCP 客户端程序 ===
import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000
BUFLEN = 512

# 实例化一个socket对象，指明协议
tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务器端socket
tcp_client_socket.connect((SERVER_IP,SERVER_PORT))

while True:
    # 从终端读入用户输入的字符串
    toSend = input('>> ')
    if toSend == '':
        break

    # 发送消息，需要将字符串编码为bytes
    tcp_client_socket.send(toSend.encode('utf-8'))

    # 等待接收服务器端的消息
    recved = tcp_client_socket.recv(BUFLEN)

    # 如果返回空bytes，表示对方关闭了连接
    if not recved:
        break

    # 打印读取的信息
    print(recved.decode("utf-8"))

# 关闭socket连接
tcp_client_socket.close()