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

    print("-------1------")
    # 4.等待客户端的链接 accept (阻塞)
    new_client_socket,client_addr = tcp_server_socket.accept()
    print("-------2------")

    print(client_addr)

    # 接收客户端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data)

    new_client_socket.send("hahaha".encode("utf-8"))
    new_client_socket.close()

    # 关闭套接字
    tcp_server_socket.close()




if __name__ == '__main__':
    main()