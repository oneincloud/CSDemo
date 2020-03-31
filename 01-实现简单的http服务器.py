import socket

def service_client(connection,addr):
    '''
    为这个客户端返回数据
    :return:
    '''
    # 接收浏览器发过来的请求，即http请求
    request = connection.recv(1024)
    print(request)

    # 2.返回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据--header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    # 2.2 准备发送给浏览器的数据--body
    response += "HaHa..."

    connection.send(response.encode('utf-8'))

    # 关闭套接字
    connection.close()


def main():
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2. 绑定
    tcp_server_socket.bind(("",7890))


    # 3.变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4.等待新客户端的连接
        new_socket,client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket,client_addr)

    # 关闭套接字
    tcp_server_socket.close()



if __name__ == "__main__":
    main()