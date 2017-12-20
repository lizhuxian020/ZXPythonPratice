# coding: utf-8
# Author: lee_zix

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 8123))
s.listen(8)

while 1:
    connect, address = s.accept()
    buf = connect.recv(10)
    connect.send(buf)

s.close()