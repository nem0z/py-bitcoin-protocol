import socket
import time

import utils

from message import Message

from messages import ping
from messages import version
from messages import verack

class Client():
    def __init__(self, peer_ip, peer_port):
        self.peer_ip = peer_ip
        self.peer_port = peer_port
        self.sock = socket.socket()

    def connect(self):
        self.sock.settimeout(5.0)
        self.sock.connect((self.peer_ip, self.peer_port))
        
        self.version()
        payload, header = self.read()
        print("Version :\nHeader :", header,"\nPayload :", payload, end="\n\n")
        
        self.verack()
        payload, header = self.read()
        print("Verack :\nHeader :", header,"\nPayload :", payload, end="\n\n")
       
        self.clear()

    def version(self):
        version_message = version.message(self.peer_ip)
        self.sock.send(version_message.get())
    
    def verack(self):
        verack_message = verack.message()
        self.sock.send(verack_message.get())

    def ping(self):
        msg = ping.message()
        self.sock.send(msg.get())
        resp_message = utils.to_bytes_fixed_size(bytes("pong", "ascii"), 12)
        
        payload, header = self.read()
        while header[4:16] != resp_message and len(header) > 0:
            payload, header = self.read()
        
        return payload == msg.payload
    
    def getaddr(self):
        msg = Message("getaddr", bytes())
        self.sock.send(msg.get())
        payload, _ = self.read()
        if payload == None:
            return []
        size, _ = utils.parse_var_int(payload[:9])
        
        list_addr = utils.chunk_to_list(payload[size:], 30)
        return [utils.parse_addr(addr) for addr in list_addr]
    
    def clear(self):
        time.sleep(.5)
        try:
            while True:
                data = self.sock.recv(1024)
                print("Clear", len(data), "bytes")
                if len(data) < 1024:
                    break
        except socket.timeout:
            return
    
    def read(self):
        header = self.sock.recv(24)
        payload_length = int.from_bytes(header[16:20], 'little')
        payload = self.sock.recv(1024)
        
        while(len(payload) < payload_length):
            payload += self.sock.recv(1024)
        
        checksum = header[20:24]
        payload_checksum = utils.checksum(payload)
        
        if payload_checksum == checksum:
            return (payload, header)
        else:
            return None, header