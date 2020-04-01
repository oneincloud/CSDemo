import socket

def main():
    '''
    主函数
    :return:
    '''
    # 1.创建tcp套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定本地信息
    tcp_server_socket.bind(("",7788))

    # 3.让默认的套接字由主动变被动listen
    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4.等待客户端的链接 accept (阻塞)
        new_client_socket,client_addr = tcp_server_socket.accept()

        print("一个新的客户端已经到来%s" % (str(client_addr)))

        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是：%s" % recv_data.decode("utf-8"))

            # 如果recv解堵塞，那么有2种方式：
            # 1. 客户端发送过来数据
            # 2. 客户端调用close导致了 这里 recv解堵塞

            if recv_data:
                # 回送一部份数据给客户端
                new_client_socket.send("hahaha".encode("utf-8"))
            else:
                break

        new_client_socket.close()

    # 关闭套接字
    tcp_server_socket.close()




if __name__ == '__main__':
    main()