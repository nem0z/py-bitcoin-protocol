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
        return self.sock.recv(24)

    def ping(self):
        ping_message = ping.message()
        self.sock.send(ping_message.get())
        return self.sock.recv(128)