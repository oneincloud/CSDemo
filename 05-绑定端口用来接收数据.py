import socket

def main():
    # 1. 创建套接字
    upd_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2. 绑定一个本地端口
    localaddr = ('',7788)
    upd_socket.bind(localaddr)

    print("服务器已启动：%s" % (str(localaddr)))

    while True:
        # 3. 接收数据
        recv_msg,addr = upd_socket.recvfrom(1024)

        # recv_msg = recv_msg.decode('utf-8')
        recv_msg = recv_msg.decode('gbk')

        # 4.打印接收到的数据
        print("接收到客户端%s的消息：%s" % (addr,recv_msg))

        if recv_msg == "exit":
            break


    # 5. 关闭套接字
    upd_socket.close()

if __name__ == "__main__":
    main()