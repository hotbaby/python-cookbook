
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial

class LazyConnection(object):
    
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock != None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock
    
    def __exit__(self, exec_ty, exec_val, tb):
        self.sock.close()
        self.sock = None
        

class LazyConnections(object):
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []
        
    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock
        
    def __exit__(self, exec_ty, exec_val, tb):
        self.connections.pop().close()
        
    
if __name__ == '__main__':
    with LazyConnection(('www.python.org',  80)) as s:
        s.send(b'GET /index.html HTTP/1.0\r\b')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)