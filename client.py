import socket
import time

import utils

from messages import ping
from messages import version
from messages import verack

class Client():
    def __init__(self, peer_ip, peer_port):
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.sock = socket.socket()

    def connect(self):
        self.sock.connect((self.peer_ip, self.peer_port))
        version_message = version.message(self.peer_ip)
        self.sock.send(version_message.get())
    
    def verack(self):
        verack_message = verack.message()
        self.sock.send(verack_message.get())

    def ping(self):
    def clear(self):
        try:
            while True:
                data = self.sock.recv(1024)
                print("Clear", len(data), "bytes")
                if not data:
                    break
        except socket.timeout:
            return
    def read(self):
        header = self.sock.recv(24)
        payload_length = int.from_bytes(header[16:20], 'little')
        payload = self.sock.recv(payload_length)
        checksum = header[20:24]
        payload_checksum = utils.checksum(payload)
        
        if payload_checksum == checksum:
            return (payload, header)
        else:
            return None, header