import socket

# 定义一个类来储存请求的信息
class Request(object):

    def __init__(self):
        # 请求方法一般为 get 或者 post
        self.method = 'GET'
        self.path = ''
        self.body = ''

request = Request()

def response_for_path(path):
    r = {
        '/': route_index,
    }

    response = r.get(path,error)

    return response()

def route_index():
    hreader = 'HTTP/1.1 200 OK\r\nContent-type: text/html\r\n'
    body = template('index.html')
    r = hreader + '\r\n' + body
    return r.encode(encoding='utf-8')

def template(fname):
    path = 'templates/' + fname
    with open(path,'r',encoding='utf-8') as f:
        return f.read()

def error(code=404):
    error_dict = {
        404:b'HTTP/1.1 404 NOT FOUND\r\n\r\n<h1>404 NOT FOUND</h1>'
    }
    return error_dict.get('code',b'')

def run(host='',port=3000):
    # 创建一个socket对象
    # s = socket.socket()
    with socket.socket() as s:

        # 绑定 host 和 port
        s.bind((host,port))

        while True:
            # 用 listen 监听请求
            s.listen(3)
            # connection 是连接
            connection,address = s.accept()
            # 用recv接收客户端发送的请求数据
            r = connection.recv(1024)
            # 网络上传输过来的也是bytes类型，所以要将bytes 转回 str
            r = r.decode('utf-8')
            print('r 请求的数据长什么样子', r)
            # 防止空请求报错，加一层保险
            if len(r.split()) < 2:
                continue

            request.method = r.split()[0]
            request.body = r.split('\r\n\r\n')[1]
            request.path = r.split()[1]

            response = response_for_path(request.path)

            connection.sendall(response)
            connection.close()

if __name__ == '__main__':
    run()
