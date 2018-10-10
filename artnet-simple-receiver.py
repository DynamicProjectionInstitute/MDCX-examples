#!/usr/bin/python
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock.bind(('0.0.0.0',6454))

while True:
        data = sock.recv(10240)
        if len(data) < 20:
                continue
        if data[0:7] != "Art-Net" or data[7] != "\0":
                continue
        if ord(data[8]) != 0x00 or ord(data[9]) != 0x50:
                continue
        dmx = data[18:]
        r = [hex(ord(c)) for c in dmx]
        print
        print r
