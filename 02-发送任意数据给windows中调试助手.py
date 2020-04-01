import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        # 从键盘或取数据
        send_data = input("请输入要发送的数据：")

        if send_data == "exit":
            break

        send_data += "\n"   # 接收换行

        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode('utf-8'),('10.0.0.16',8080))    # 发送到网络助手测试

    # 关闭socket
    udp_socket.close()

if __name__ == '__main__':
    main()